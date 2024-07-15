# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

 

# Constraints:

#     1 <= s.length, t.length <= 5 * 104
#     s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = {}
        map_t = {}

        for i in range(len(s)):
            if s[i] not in map_s:
                map_s[s[i]] =1
            else:
                map_s[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in map_t:
                map_t[t[j]] =1
            else:
                map_t[t[j]] += 1

        return map_s == map_t