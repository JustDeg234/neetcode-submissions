class Solution:
    def trap(self, height: List[int]) -> int:
        #Create an equation for area of water given height of bars
        # conditions: water must be trapped bewteen adjacent bars
        # Area of water = 1 * height = height of water
        # Sum from 0 to height_list - 1: A_max(height) = Hw_max = min(hb_left, hb_right) - hb_i
        #Need: List of calculated min height of adjacent bars per element 
        
        #Naive Approach
        Area_Sum = 0
        for i in range(len(height)):
            hb_left_max = max(height[:i+1])
            hb_right_max = max(height[i:]) #im thinking of convolution, stepping out of Area(h) domain to this graph, but instead in terms of dimension (set)
            Area_Sum += min(hb_left_max, hb_right_max) - height[i]
        return Area_Sum