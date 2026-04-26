class Solution:
    def threeSum(self, nums:List[int]) -> List[List[int]]:
        #return List of three distinct integers (from each other within the list and set) that add to 0
        #Brute force: Attempt every possible triplet by first sorting and adding all to a set
        working_principle = set(); #O(1) lookup during every check
        nums.sort() #Sorting algortihm O(nlogn) onto array in place
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in  range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        #Wish to append [nums[i], nums[j], nums[k]]
                        temp = [nums[i], nums[j], nums[k]];
                        working_principle.add(tuple(temp)); #set only accepts immutable values
                        #Set ensures no duplicates, O(n^3) time, O(m) space where m is the number of triplets
        return [list(i) for i in working_principle]


