'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

'''Logic:
1. Check if the list is empty.
2. Pick the first word as the reference.
3. Compare each character (by index) of the first word with all other words.
4. Stop and return everything before the first mismatch.
5. If no mismatch is found, return the first word as the prefix.'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first = strs[0]
        for i, ch in enumerate(first):
            for w in strs[1:]:
                if i == len(w) or w[i] != ch:
                    return first[:i]
        return first
                
