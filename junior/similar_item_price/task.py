from typing import Dict
from typing import List
from typing import Tuple
from itertools import combinations
import numpy as np
from scipy.spatial.distance import cosine


class SimilarItems:
    """Similar items class"""

    @staticmethod
    def similarity(embeddings: Dict[int, np.ndarray]) -> Dict[Tuple[int, int], float]:
        """Calculate pairwise similarities between each item
        in embedding.

        Args:
            embeddings (Dict[int, np.ndarray]): Items embeddings.

        Returns:
            Tuple[List[str], Dict[Tuple[int, int], float]]:
            List of all items + Pairwise similarities dict
            Keys are in form of (i, j) - combinations pairs of item_ids
            with i < j.
            Round each value to 8 decimal places.
        """
        similarities = {}
        for pair in combinations(embeddings.keys(), 2):
            similarities[pair] = round(1 - cosine(embeddings[pair[0]], embeddings[pair[1]]), 8)
        return similarities

    @staticmethod
    def knn(
        sim: Dict[Tuple[int, int], float], top: int
    ) -> Dict[int, List[Tuple[int, float]]]:
        """Return closest neighbors for each item.

        Args:
            sim (Dict[Tuple[int, int], float]): <similarity> method output.
            top (int): Number of top neighbors to consider.

        Returns:
            Dict[int, List[Tuple[int, float]]]: Dict with top closest neighbors
            for each item.
        """
        knn_dict = {}

        for pair, value in sim.items():
            if pair[0] not in knn_dict:
                knn_dict[pair[0]] = [(pair[1], value)]
            else:
                knn_dict[pair[0]].append((pair[1], value))
                knn_dict[pair[0]] = sorted(knn_dict[pair[0]], key=lambda x: x[1], reverse=True)[:top]

            if pair[1] not in knn_dict:
                knn_dict[pair[1]] = [(pair[0], value)]
            else:
                knn_dict[pair[1]].append((pair[0], value))
                knn_dict[pair[1]] = sorted(knn_dict[pair[1]], key=lambda x: x[1], reverse=True)[:top]

        return knn_dict

    @staticmethod
    def knn_price(
        knn_dict: Dict[int, List[Tuple[int, float]]],
        prices: Dict[int, float],
    ) -> Dict[int, float]:
        """Calculate weighted average prices for each item.
        Weights should be positive numbers in [0, 2] interval.

        Args:
            knn_dict (Dict[int, List[Tuple[int, float]]]): <knn> method output.
            prices (Dict[int, float]): Price dict for each item.

        Returns:
            Dict[int, float]: New prices dict, rounded to 2 decimal places.
        """
        knn_price_dict = {}
        for product, similar in knn_dict.items():

            for i in range(len(similar)):
                similar[i] = (prices[similar[i][0]], similar[i][1])
            
            similar = np.array(similar)
            knn_price_dict[product] = round(np.sum(similar[:, 0] * (similar[:, 1] + 1))/np.sum(similar[:, 1] + 1), 2)

        return knn_price_dict

    @staticmethod
    def transform(
        embeddings: Dict[int, np.ndarray],
        prices: Dict[int, float],
        top: int,
    ) -> Dict[int, float]:
        """Transforming input embeddings into a dictionary
        with weighted average prices for each item.

        Args:
            embeddings (Dict[int, np.ndarray]): Items embeddings.
            prices (Dict[int, float]): Price dict for each item.
            top (int): Number of top neighbors to consider.

        Returns:
            Dict[int, float]: Dict with weighted average prices for each item.
        """
        similarities = SimilarItems.similarity(embeddings)
        neighbours = SimilarItems.knn(similarities, top)
        knn_price_dict = SimilarItems.knn_price(neighbours, prices)
        return knn_price_dict
