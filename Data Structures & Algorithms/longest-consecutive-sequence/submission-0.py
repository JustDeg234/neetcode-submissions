class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        hs = set(nums) #Offers O(1) lookup time while comparing each num with consecutive
        for num in nums: #O(n) 
            count, curr = 0, num
            while curr in hs: #O(n) at worst
                count += 1
                curr += 1
            output = max(output, count)
        return output #O(n^2) brute force