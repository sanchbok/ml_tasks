from typing import List
from typing import Tuple


def extend_matches(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    ''' Find all matches between pairs '''
    matches = {}
    pairs_copy = list(map(sorted, pairs))

    for pair in pairs_copy:
        matches[pair[0]] = pair[1:]

    all_matches = []
    for main_item in list(matches):
        if main_item in matches:
            additional_items = matches[main_item]

            for additional_item in additional_items:
                if additional_item in matches:
                    additional_items.extend(matches[additional_item])
                    del matches[additional_item]

            new_match = tuple(sorted(set([main_item] + additional_items)))
        else:
            continue

        all_matches.append(new_match)

    return sorted(all_matches)
