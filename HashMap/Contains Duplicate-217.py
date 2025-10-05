'''Given an integer array nums, return true if any value appears at least twice in the array, and
return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.'''

'''Logic:
* Use a dictionary to keep track of the elements we have seen so far.
* Iterate through each element in the array:
    - If the element is already in the dictionary, return True (indicating a duplicate).
    - If the element is not in the dictionary, add it to the dictionary.'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i in nums:
            if i in seen:
                return True
            else:
                seen[i] = index
        return False
