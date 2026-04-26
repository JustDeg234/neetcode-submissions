class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums)) #convert list to set and compare lengths (duplicate discarded)