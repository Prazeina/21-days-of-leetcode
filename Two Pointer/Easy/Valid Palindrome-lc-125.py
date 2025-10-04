'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

'''
'''Logic:
* Convert all characters to lowercase.
* Keep only alphanumeric characters (letters and numbers).
    ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']
* Create a cleaned string from the filtered characters.
    amanaplanacanalpanama
* Reverse the cleaned string.
    amanaplanacanalpanama
* Compare the cleaned string with its reversed version. If they are the same, the original string is a palindrome; otherwise, it is not.'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower=s.lower()
        cleaned_chars = []
        for i in s_lower:
            if i.isalnum():
                cleaned_chars.append(i)
        print(cleaned_chars)
        cleaned_string = "".join(cleaned_chars)
        reversed_string = cleaned_string[::-1]
        if cleaned_string == reversed_string:
            return True
        else:
            return False
  