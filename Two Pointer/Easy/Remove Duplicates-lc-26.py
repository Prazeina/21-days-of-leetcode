'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

'''Logic:
* Initialize an empty set to keep track of seen elements.
* Initialize a pointer i to 0, which will indicate the position to place the next unique element.
* Iterate through each element n in the input array nums: if n is not in seen set, place n at index i in nums
and increment i by 1. Add n to the seen set.'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        i = 0  

        for n in nums:
            if n not in seen:
                nums[i] = n  
                i = i+1
                seen.add(n)
        return i