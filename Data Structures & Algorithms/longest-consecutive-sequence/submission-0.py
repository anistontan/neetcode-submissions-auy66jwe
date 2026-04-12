class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        best=0

        for x in numset:
            if (x-1) not in numset:
                length=1
                while (x+length) in numset:
                    length+=1
                best=max(best,length)
        return best    
