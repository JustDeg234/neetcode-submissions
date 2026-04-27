class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {} #key: unique elements, value: frequency
        for n in nums:
            hm[n] = hm.get(n, 0) + 1
        return sorted(hm, key=lambda x: hm[x], reverse=True)[0:k]
