class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        use two pointers l and r but NOT like the container problem 
        you maintain : 
        - leftMax = tallest seen so far from left 
        - rightMax = tallest seen so far from right 
        - water = 0 0
        then repeatedly  
        - compare height[l] and height[r]
        - move the side with the smaller height inward
        - update the side's max 
        - add trapped water at that side :maxSoFar - currentHeight (if positive)
        why this works : 
        the smallest side limits the water level for that side 
        '''

        leftMax=0
        rightMax=0
        l=0
        r=len(height)-1
        water=0

        while l<r:
            if height[l]<height[r]: #left is smaller
                leftMax=max(leftMax,height[l])
                water+=leftMax-height[l] 
                '''
                leftMax=tallest bar we've seen so far on the left side
                height[l] = the current bar's height 
                if the left wall is taller than the currentbar, the difference is empty space that can be filled with water:
                    water on this bar = leftMax-height[l]
                if the current bar is tall enough to be the new left wall, then :
                    leftMax==height[l] --> leftMax-height[l]=0 --> no water added 
                '''
                l+=1
            else:
                rightMax=max(rightMax,height[r])
                water+=rightMax-height[r]
                r-=1
        
        return water











