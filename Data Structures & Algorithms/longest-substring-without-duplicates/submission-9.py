class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, output = 0, 0
        hm = {} #last index lookup
        for r in range(len(s)):
            if s[r] in hm:
                l = max(l, hm[s[r]] + 1) 
            hm[s[r]] = r
            output = max(r - l + 1, output)
        return output