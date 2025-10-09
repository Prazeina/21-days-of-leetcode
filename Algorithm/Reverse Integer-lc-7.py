'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer 
range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321'''

'''Logic:
* Handle the sign of the integer.
* Use a loop to extract digits from the integer and build the reversed integer.'''

class Solution:
    def reverse(self, x: int) -> int:
        int_max = 2**31 - 1  
        int_min = -2**31    

        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        while x != 0:
            pop = x % 10
            x //= 10

            if rev > (int_max - pop) // 10:
                return 0

            rev = rev * 10 + pop

        return sign * rev
