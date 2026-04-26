class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search on already sorted array of int, O(logn)
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r-l)//2 #avoids overflow in lower level programs
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1