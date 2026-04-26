class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute force: attempt every possible triplet with restriction i<j<k
        working_principle = set() #O(1) lookup
        nums.sort() #O(nlogn)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        #Cant add mutable object into set
                        temp = [nums[i], nums[j], nums[k]]
                        working_principle.add(tuple(temp)) #current return type is set
        output = []
        for i in working_principle:
            output.append(list(i))
        return output

