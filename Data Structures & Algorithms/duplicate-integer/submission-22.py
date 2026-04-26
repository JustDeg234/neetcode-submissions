class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() #List method to sort O(logn)
        for i in range(1, len(nums)): #O(n)
            if nums[i] == nums[i-1]: 
                return True #total: O(n + nlogn) = O(nlogn)
        return False
