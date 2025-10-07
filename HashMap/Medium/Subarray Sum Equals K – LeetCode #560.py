'''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2'''

'''Logic:
* Use a hashmap to store the cumulative sum and its frequency.
* Initialize a variable to keep track of the current sum and a count of valid subarrays.
* Iterate through the array, updating the current sum and checking if (current sum - k) exists in the hashmap.
* If it exists, it means there are subarrays ending at the current index which sum to k.
* Update the hashmap with the current sum.
* Finally, return the count of valid subarrays.'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int) #Store cumulative frequencies
        current_sum = 0 # Store Current sum as we iterate
        total = 0 #Total sub arrays that resulted in k
        
        for num in nums:
            current_sum = current_sum + num #update cumulative sum
            if current_sum == k:
                total = total + 1 #current
            else:
                pass
            
            if current_sum - k in seen:
                total = total + seen[current_sum - k]
            else:
                pass

            seen[current_sum] = seen[current_sum] + 1 #Update seen dictionary with current cumulative sum
        
        return total