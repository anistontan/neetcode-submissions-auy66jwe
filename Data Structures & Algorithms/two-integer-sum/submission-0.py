class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={} #create a dictionary 
        #{number:index, ...} eg{2:0} value 2 was seen at index 0
        for i in range(len(nums)): #go through the array
            need=target-nums[i] #what we need
            if need in seen: #if what we need is alr in the dictionary
                j=seen[need] #retrieve the index (need is the value we want)
                return [min(i,j),max(i,j)]
            seen[nums[i]]=i #if not we add the {value(nums[i]), index(i)}