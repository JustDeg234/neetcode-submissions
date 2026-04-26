class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Goal: avoiding KeyError by utilizing collections.Counter for counting hashable objects
        return Counter(s) == Counter(t)