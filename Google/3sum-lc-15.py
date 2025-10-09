'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.'''

'''Logic:
* Sort the input list to facilitate the two-pointer technique and handle duplicates.
Use two pointers left and right to find pairs, right from end of the list and left from the next element of i.
sum of three elements is calculated and compared to zero.
if sum is less than zero, increment left pointer to increase the sum.
if sum is greater than zero, decrement right pointer to decrease the sum.
if sum is zero, add the triplet to the result list and move both pointers to find other potential triplets.
Skip duplicate elements to avoid repeating the same triplet in the result.'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [ ]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left = left+1
                elif total > 0:
                    right = right-1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left_val, right_val = nums[left], nums[right]

                    #Skip duplicate from left
                    while left<right and nums[left] == left_val:
                        left = left+1
                    #Skip duplicate from right
                    while left<right and nums[right] == right_val:
                        right = right-1
        return result


