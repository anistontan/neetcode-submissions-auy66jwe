class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        suppose a bar has height h 
        if it is the shortest bar in some rectangle, then that rectangle can stretch across 
        all consecutive bars with height at least h 
        so when we "pop" a bar from the stack, we are basically saying : 
        area= h * width 

        KEY FORMULA : 
        when popping an index top : 
        - height = heights[top]
        - right boundary = current index i 
        - left boundary = new top of stack after popping 
        so : 
        if stack becomes empty, width = i 
        otherwise, width= i - stack[-1] - 1 
        bcuz after popping 
        - stack[-1] is the nearest smallest bar on the left 
        - i is the first smaller bar on the right 
        '''

        stack = [] #store indices 
        # we keep indices of bars in an increasing height order
        max_area = 0

        heights.append(0) #add a sentinel 0 to flush the stack at the end 

        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                h=heights[stack.pop()]

                if not stack: 
                    width=i
                else: 
                    width = i - stack[-1] -1 
                
                max_area=max(max_area, h*width)
            
            stack.append(i)
        return max_area