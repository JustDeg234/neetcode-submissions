class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set() #O(1) lookup, insertion, reorder
        for n in nums: #O(n)
            if n in hs:
                return True
            hs.add(n)
        return False
        