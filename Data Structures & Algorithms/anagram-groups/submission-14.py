class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {} #key: freq tuple of each string, value: list of strings
        for s in strs:
            count = [0] * 26
            for c in s: # O(n * m)
                count[ord(c) - ord('a')] += 1 #parse by letter to num
            keyable_cnt = tuple(count)
            if keyable_cnt not in freq:
                freq[keyable_cnt] = []
            freq[keyable_cnt].append(s)
        return list(freq.values())