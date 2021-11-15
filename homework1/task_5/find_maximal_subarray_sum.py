from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    counter = 0  # counter for the loop condition
    loop_counter = len(nums) - k  # counter for the loop condition
    sum_list = []
    if len(nums) == 1:
        return nums[0]
    while counter <= loop_counter:
        sum_list.append(sum(nums[counter : counter + k]))
        counter += 1
    return max(sum_list)
