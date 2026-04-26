class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                container = min(heights[i], heights[j]) * (j-i) #returns biggest area this specific container could be
                #constantly update max container area
                output = max(output, container)
        return output