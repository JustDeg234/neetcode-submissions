class Solution:
    def findMin(self, nums: List[int]) -> int:
        output = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]: #sorted array is bounded by l and r, return l (guaranteed min)
                output = min(output, nums[l])
                break

            #binary search
            m = (l + r) // 2 
            output = min(output, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1 #slides windows of search 
            else:
                r = m - 1
        return output