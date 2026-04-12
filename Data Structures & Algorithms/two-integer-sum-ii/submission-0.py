class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        1. put one pointer at the start (l)
        2. one at the end (r)
        3. check numbers[l] + numbers[r]
        - if too small, move l to right (to increase sum)
        - if too big, move r to left (to decrease sum)
        - if it matches, return (remember: 1 indexed)
        '''

        l=0
        r=len(numbers)-1

        while l<r:
            cur= numbers[l]+numbers[r]
            if cur < target: 
                l+=1
            elif cur > target: 
                r-=1
            else: 
                return [l+1,r+1]









