from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    result = []
    for element in args[0]:
        result.append([element])
    for new_list in args[1:]:
        new_result = []
        for element in result:
            for elem in new_list:
                new_result.append(element + [elem])
        result = new_result
    return result
