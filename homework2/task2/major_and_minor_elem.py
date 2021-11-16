from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    sequence = sorted(inp)
    occurrences = 0
    current_element = sequence[0]
    temp_seq = []
    for element in sequence:
        if element == current_element:
            occurrences += 1
        else:
            temp_seq.append((occurrences, current_element))
            current_element = element
            occurrences = 1
    temp_seq.append((occurrences, current_element))
    temp_seq.sort()
    return temp_seq[-1][1], temp_seq[0][1]
