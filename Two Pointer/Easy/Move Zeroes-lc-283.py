'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]'''
# Two Solutions

'''Logic:
* Initialize a pointer last_non_zero to 0, which will track the position to place the next non-zero element.
* Iterate through the array with an index i. For each element:
    - If the element is non-zero, swap it with the element at last_non_zero index
    - Increment last_non_zero by 1.'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero = 0  # position to place the next non-zero number

        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap the current element with the last_non_zero position
                nums[i], nums[last_non_zero] = nums[last_non_zero], nums[i]
                last_non_zero = last_non_zero + 1

'''Logic:
* Create a new list to store non-zero elements.
* Iterate through the original list and append all non-zero elements to the new list.
* Count the number of zeroes in the original list.
* Extend the new list by adding the counted number of zeroes at the end.
* Copy the elements from the new list back to the original list to modify it in-place.'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_list=[]
        for num in nums:
            if num!=0:
                new_list.append(num)
        
        zeroes_count=nums.count(0)

        new_list.extend([0]*zeroes_count)

        for i in range(len(nums)):
            nums[i] = new_list[i]