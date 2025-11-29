# https://leetcode.cn/problems/find-pivot-index
from typing import List


class Solution:
    def pivotIndex_slow(self, nums: List[int]) -> int:
        all_sum = sum(nums)

        for i in range(len(nums)):
            if i == 0:
                left_sum = 0
                right_sum = all_sum - nums[i]
            elif i == len(nums) - 1:
                right_sum = 0
                left_sum = all_sum - nums[i]
            else:
                left_sum = sum(nums[:i])
                right_sum = sum(nums[i + 1 :])

            if left_sum == right_sum:
                return i

        return -1

    def pivotIndex(self, nums: List[int]) -> int:
        all_sum = sum(nums)

        for i in range(len(nums)):
            if i == 0:
                left_sum = 0
                right_sum = all_sum - nums[i]
            else:
                left_sum += nums[i - 1]
                right_sum -= nums[i]

            if left_sum == right_sum:
                return i

        return -1
