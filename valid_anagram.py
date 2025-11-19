LeetCode 242 – Valid Anagram


Time Complexity

O(n) – we go through each string once.

  

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1

        count_t = {}
        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1

        return count_s == count_t

Understanding:

We’re given two strings s and t.
We need to check if both are anagrams — meaning they contain the same letters, just arranged differently.


If both words are made of the same characters, then each character should appear the same number of times in both.”

So the plan was simple:

Count how many times each letter appears in the first string.

Do the same for the second string.

Compare both counts — if they match, the strings are anagrams.


Step-by-Step

                                   

Create an empty dictionary count_s to store character counts for s.

Loop through each letter in s.

If the letter is already in the dictionary, increase its count by 1.

If not, add it with count 1.

Repeat the same steps for t, storing counts in count_t.

Finally, compare both dictionaries.

If they are equal → return True

Else → return False
                                   
