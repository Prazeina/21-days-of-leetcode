'''You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.'''

'''Logic:
* Use zip to iterate through both strings simultaneously, appending characters from each to the merged list.
* After the loop, check if either string has remaining characters and append them to the merged list.
* Finally, join the list into a single string and return it.'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = [ ]

        for c1, c2 in zip(word1, word2):
            merged.append(c1)
            merged.append(c2)

        # Add remaining characters from word1, if any
        if len(word1) > len(word2):
            merged.extend(word1[len(word2):])

        # Add remaining characters from word2, if any
        if len(word2) > len(word1):
            merged.extend(word2[len(word1):])

        return "".join(merged)
