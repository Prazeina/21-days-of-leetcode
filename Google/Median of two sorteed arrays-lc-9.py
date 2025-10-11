'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.'''

'''Logic:
1. Merge the two sorted arrays.
2. Sort the merged array.
3. Find the median of the sorted merged array.
4. For median, get the index of the middle element(s) based on the length of the array (odd/even).'''

import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged = sorted(nums1 + nums2)   # just merge & sort
        n = len(merged)
        
        if n % 2 == 1:   
            return merged[n // 2]
        else:            
            return (merged[n // 2 - 1] + merged[n // 2]) / 2

