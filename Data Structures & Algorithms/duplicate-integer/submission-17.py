class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = set() #more than once -> hashset
        for i in range(len(nums)):
            if nums[i] in cnt:
                return True
            cnt.add(nums[i])
        return False