from typing import List, Optional, Sequence, TypeVar

T = TypeVar("T")


def custom_range(
    sequence: Sequence[T],
    first: T,
    second: Optional[T] = None,
    third: Optional[int] = None,
    /,
) -> List[T]:
    if second is None:
        start, stop = sequence[0], first
    else:
        start, stop = first, second
    if third is not None:
        step = third
    else:
        step = 1

    if step < 0:
        sequence = list(reversed(sequence))

    start_index, stop_index = None, None
    for index, element in enumerate(sequence):
        if element == start and start_index is None:
            start_index = index
        if element == stop and stop_index is None:
            stop_index = index
        if None not in (start_index, stop_index):
            break

    if start_index >= stop_index:
        return []

    return list(sequence)[start_index : stop_index : abs(step)]
