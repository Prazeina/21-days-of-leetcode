'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to 
target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]'''

'''Logic:
* Use a dictionary to store the numbers we have seen so far and their indices.
* For each number in the array, calculate its complement (target - current number).
* Check if the difference exists in the dictionary:
    - If it does, return the indices of the current number and the complement.
    - If it doesn't, add the current number and its index to the dictionary.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 
        
        for index, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                return [seen[difference], index]
            else:
                seen[num] = index


