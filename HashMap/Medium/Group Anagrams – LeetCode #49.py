'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]'''

'''Logic:
* Use a dictionary to group anagrams together.
* For each string in the input list, sort the characters in the string to create a key.
* Use this sorted string as a key in the dictionary, and append the original string to the list of anagrams for that key.
* Finally, return the values of the dictionary as a list of lists.'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))  
            groups[key].append(s) #based on key append the s ie string
        return list(groups.values()) #converts the view object into a list

