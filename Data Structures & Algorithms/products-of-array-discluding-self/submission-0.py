class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #initalize arrays
        prefix, suffix, output = [1] * n, [1] * n, [1] * n

        for i in range(1, n):
            prefix[i] =  nums[i-1] * prefix[i-1]
        for i in range(n-2, -1,-1): #stop at 0 including 0, start at the 2nd to last element, iterate down
            suffix[i] = nums[i+1] * suffix[i+1]
        for i in range(n):
            output[i] = prefix[i] * suffix[i]
        return output