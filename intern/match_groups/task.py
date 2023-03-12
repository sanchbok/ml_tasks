from typing import List
from typing import Tuple


def extend_matches(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    ''' Find all matches between pairs '''
    matches = dict(sorted([(i, j) if i < j else (j, i) for i, j in pairs]))

    all_matches = []
    for main_item, additional_item in matches.items():
        all_matches.append((main_item, additional_item))
        while additional_item in matches:
            new_item = matches[additional_item]
            all_matches.append((main_item, new_item))
            additional_item = new_item

    return all_matches
