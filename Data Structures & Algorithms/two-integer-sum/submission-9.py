class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #FP: target - current num and scan hashmap keyed via element and valued by the indices, due to nature of hash lookup by unique keys
        hm = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hm:
                return [hm[compliment], i]
            hm[nums[i]] = i
        return []