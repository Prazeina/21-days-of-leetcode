'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.'''

'''Logic:
1. Convert the integer to a string.
2. Reverse the string using slicing.
3. Convert the reversed string back to an integer.
4. Compare the reversed integer with the original integer.'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        x_reverse = int(str(x)[::-1])

        if x_reverse == x:
            return True
        else:
            return False