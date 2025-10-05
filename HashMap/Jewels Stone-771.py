'''You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3'''

'''Logic:
* Use a dictionary to count the occurrences of each stone in the stones string.
* Iterate through each jewel in the jewels string and sum up the counts from the 
  count_stones dictionary to get the total number of jewels in stones.'''

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count_stones = {}
        for stone in stones:
            if stone in count_stones:
                count_stones[stone] = count_stones[stone] + 1
            else:
                count_stones[stone] = 1

        total = 0
        for jewel in jewels:
            if jewel in count_stones:
                total = total + count_stones[jewel]

        return total

# OR

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count_stones = Counter(stones)

        total = 0
        for jewel in jewels:
            if jewel in count_stones:
                total = total + count_stones[jewel]

        return total
