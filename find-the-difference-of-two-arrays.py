# https://leetcode.cn/problems/find-the-difference-of-two-arrays
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1_set = set(nums1)
        s2_set = set(nums2)

        merge_set = set(nums1 + nums2)
        return [list(merge_set - s2_set), list(merge_set - s1_set)]
