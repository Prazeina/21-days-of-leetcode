'''https://leetcode.com/problems/reorganize-string'''

'''Logic:
Use a counter to count the frequency of each character.
If the maximum frequency is more than (n + 1) // 2, return "".
Place the most frequent character at even indices first, then fill in the rest.'''

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        n = len(s)
        max_char, max_count = max(count.items(), key=lambda x: x[1])
        
        # If impossible
        if max_count > (n + 1) // 2:
            return ""
        
        res = [""] * n
        i = 0  # even index

        # Place the most frequent character first
        while count[max_char] > 0:
            res[i] = max_char
            count[max_char] = count[max_char] - 1
            i = i + 2

        # Fill in the remaining characters
        for ch, freq in count.items():
            while freq > 0:
                if i >= n:  # move to odd indices
                    i = 1
                res[i] = ch
                i = i + 2
                freq = freq - 1
        
        return "".join(res)