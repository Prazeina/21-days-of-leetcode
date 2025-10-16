'''Logic: 
Use a stack to keep track of opening brackets. 
For each closing bracket, check if it matches the most recent opening bracket. 
If it does, pop the stack; if not, return false. At the end, if the stack is empty, all brackets matched correctly.'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            # If it's an opening bracket, push its matching closing bracket
            if char in pairs:
                stack.append(pairs[char])
            
            # If it's a closing bracket but stack is empty → no match
            elif not stack:
                return False
            
            # If it's a closing bracket and it doesn't match the expected one
            elif stack.pop() != char:
                return False

        # If stack is empty at the end, all brackets matched
        return not stack
