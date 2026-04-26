class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        for i in range(len(s)):
            hs = set() #create new hashset every letter
            for j in range(i, len(s)):
                if s[j] in hs:
                    break
                hs.add(s[j])
            output = max(len(hs), output)
        return output