class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #without duplicate, use hm
        output, l = 0, 0
        hs = set()
        for c in range(len(s)): #in python, can parse string as list of chars
            while s[c] in hs: #base case: reached dupe, move left pointer
                hs.remove(s[l])
                l += 1 #left pointer that sweeps last substring, max lgenth always stored in output
            hs.add(s[c])
            output = max(c - l + 1, output)
        return output