class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case, check string lengths, also handles case of s > t or vice versa when they share equal letters up until one exceeds the others' length
        if (len(s) != len(t)): return False

        hm = {} #key: char, value: freq
        for c in s:
            hm[c] = hm.get(c, 0) + 1
        
        for c in t:
            if c not in hm: #if hm[c] == 0: causes keyerror when c in t wasnt in s, thus python sees 'm' and tries to return, causing a key error
                return False
            hm[c] -= 1
            if hm[c] < 0:
                return False

        return True