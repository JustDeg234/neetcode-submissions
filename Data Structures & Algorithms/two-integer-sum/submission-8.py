class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt = {} #key: element value: index (swapped due to requested output of indices)
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in cnt:
                return [cnt[compliment], i] #stored index is naturally less than current index
            cnt[nums[i]] = i
        return []

