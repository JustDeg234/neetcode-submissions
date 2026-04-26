class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False

        hm = {} #working principle: add instances of each char to a hashmap with unique keys (chars)

        for char in s:
            if char not in hm:
                hm[char] = 0
            hm[char] += 1
        
        for char in t:
            if char not in hm:
                return False
            hm[char] -= 1
            if hm[char] < 0:
                return False
        return True
