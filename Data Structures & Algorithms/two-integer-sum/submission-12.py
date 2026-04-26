class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {} #element, index
        for i in range(len(nums)):
            operand = target - nums[i]
            if operand in hm:
                return [hm[operand], i]
            hm[nums[i]] = i #store index as value, since we parse on line 5 by its associated element
        return []