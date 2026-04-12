class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # width = r-l
        # height = min(r,l)

        l=0
        r=len(heights)-1 #r should start at the last index not length
        best=0

        while l<r:
            width=r-l
            height=min(heights[l],heights[r])
            volume=width*height
            if volume > best:
                best=volume
            
            if heights[l]<heights[r]: #move the shorter side each time
                    l+=1
            else:
                r-=1
        return best