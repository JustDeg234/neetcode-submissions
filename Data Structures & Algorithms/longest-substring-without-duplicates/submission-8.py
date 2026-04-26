class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, output = 0, 0
        hs = set() #lookup O(1) used
        for r in range(len(s)):
            #base case, reached duplicate, crawl left pointer until dup removed aka new unique substring
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            output = max(r - l + 1, output)
        return output