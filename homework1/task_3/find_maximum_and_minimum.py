from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as file:
        lines = [int(line.rstrip("\n")) for line in file]
        if len(lines) < 2:
            raise ValueError("File must contain at least 2 lines with numbers")
        lines.sort()
        min_max = []
        min_max.append(lines[0])
        min_max.append(lines[-1])
        min_max_tup = tuple(min_max)
        return min_max_tup
