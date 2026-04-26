class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        for i in range(len(s)):
            hs = set()
            hs.add(s[i])
            temp = 1
            for j in range(i + 1, len(s)):
                if s[j] in hs:
                    break
                hs.add(s[j])
                temp += 1
            output = max(temp, output)
        return output
        #FIRST LEETCODE I EVER DID IN UNDER 8 MINUTES WITH the initial help of a few seconds of the neetcode video and hints of small corrections from mr g.