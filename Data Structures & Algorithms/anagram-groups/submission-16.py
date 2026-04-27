class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {} # key: char Count array, value: List of strings it is anagram with
        for s in strs:

            count = [0] * 26 #a - z elements
            for c in s:
                count[ord(c) - ord('a')] += 1 #65 - 65 = 0 for a, normalized
            key = tuple(count)

            if key not in hm: #init List value
                hm[key] = []
            hm[key].append(s)
        return list(hm.values())
                