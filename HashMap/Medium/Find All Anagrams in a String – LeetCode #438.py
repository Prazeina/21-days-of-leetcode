''' Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

''''
Logic:
* Use a sliding window and hash map to find all anagrams of p in s.
* Keep a frequency count of characters in p (p_count) and the current window in s.
* Move the window one character at a time across s.
* For each move:
    - Add the new character entering the window from right.
    - Remove the old character leaving the window from left.
* Whenever the current window’s frequency matches p_count,
  it means we found an anagram — store its starting index.
* Continue sliding the window until the end of the string.
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        k = len(p)
        p_count = Counter(p)
        window = Counter()  

        for i in range(len(s)):
            window[s[i]] = window[s[i]] + 1

            if i >= k:
                left_char = s[i - k]
                window[left_char] = window[left_char] - 1
                if window[left_char] == 0:
                    del window[left_char]

            if i >= k - 1 and window == p_count:
                result.append(i - k + 1)

        return result