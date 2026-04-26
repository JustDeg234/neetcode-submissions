class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we can guarantee i != j by hashmap referencing, and output [hm[target - i], i], operand presumed caught by hm on a previous check
        hm = {} #key: element, value: index
        for i in range(len(nums)):
            operand = target - nums[i]
            if operand in hm:
                return [hm[operand], i]
            hm[nums[i]] = i
        return []