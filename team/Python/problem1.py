import math
from typing import List

class Solution:
    """
    Solution for LeetCode problem 4
    Median of Two Sorted Arrays
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(list1, list2):
            combined = []
            i=0
            j=0

            while i < len(list1) and j < len(list2):
                if list1[i] < list2[j]:
                    combined.append(list1[i])
                    i += 1
                else:
                    combined.append(list2[j])
                    j += 1

            while i < len(list1):
                combined.append(list1[i])
                i += 1

            while j < len(list2):
                combined.append(list2[j])
                j += 1

            return combined

        sorted = merge(nums1, nums2)
        sorted_length = len(sorted)

        if sorted_length % 2 == 1:
            return sorted[math.floor(sorted_length / 2)]   
        else:
            midpoint = int((sorted_length / 2))
            return (sorted[ midpoint - 1] + sorted[ midpoint]) / 2
            