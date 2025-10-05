'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false'''

'''Logic:
* Use the Counter class from the collections module to count the frequency of each character in both strings.
* Compare the two frequency counts. If they are equal, the strings are anagrams; otherwise, they are not.'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)
        return count_s == count_t
        
# OR
'''Logic:
* Use two dictionaries to count the frequency of each character in both strings.
* Iterate through each character in the first string and update its count in the first dictionary.
* Do the same for the second string and the second dictionary.
* Finally, compare the two dictionaries. If they are equal, the strings are anagrams; otherwise, they are not.'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}

        for i in s:
            if i in seen_s:
                seen_s[i] = seen_s[i]+1
            else:
                seen_s[i]=1

        for j in t:
            if j in seen_t:
                seen_t[j] = seen_t[j]+1
            else:
                seen_t[j]=1

        return seen_s==seen_t
        
