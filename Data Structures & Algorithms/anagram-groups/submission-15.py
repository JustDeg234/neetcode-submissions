class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {} # key: sorted string, value: List of strings it is anagram with
        for s in strs:
            key = tuple(sorted(s)) # ['a', 'b', 'c']
            if key not in hm: #init List value
                hm[key] = []
            hm[key].append(s)
        return list(hm.values())
                