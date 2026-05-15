class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Input array is already sorted, O(1) space
        #2 pointer method places l and r pointers on ends of array,
        #   if arr[l] + arr[r] < sum then move left pointer forward to increase, mofe right back to decrease sum
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return [l + 1, r + 1] #return the indices (1-indexed)
        return []

