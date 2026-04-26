class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #if duplicates exist, a set() of nums will be smaller than its length
        return len(set(nums)) < len(nums)
