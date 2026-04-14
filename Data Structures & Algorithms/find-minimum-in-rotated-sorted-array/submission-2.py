class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        use 1 binary search 
        keep narrowing toward the unsorted half 
        the minimum is exactly where the rotation "break" happens
        '''
        left=0
        right=len(nums)-1

        while left<right: 
            mid=(left+right)//2

            if nums[mid] > nums[right]:
                left=mid+1
            else:
                '''
                if nums[mid]<nums[right], that means:
                - mid is in the right sorted portion 
                - the minimum could be at mid or to its left 
                '''
                right=mid 
            
        return nums[left]



