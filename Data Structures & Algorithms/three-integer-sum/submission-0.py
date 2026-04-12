class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        1. first we sort the array 
        2. for each i 
        - we use 2 pointers l, r 
        - same concept as two sum ii 
        '''

        nums.sort()
        result=[]
        n=len(nums)
        
        for i in range(n-2):
            #skip duplicate "first" numbers
            if i>0 and nums[i]==nums[i-1]:
                continue
            #optional early stop : once nums[i]>0, can't make sum 0
            if nums[i]>0:
                break 
            
            l=i+1
            r=n-1

            while l<r: 
                total = nums[i]+nums[l]+nums[r]

                if total<0:
                    l+=1
                elif total >0 :
                    r-=1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    #after we find a valid triplet, total==0
                    l+=1 #move the left pointer to the next number so we don't use the same nums[l]
                    r-=1 #move the right pointer to the previous number so ^^
                
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
        return result
                







