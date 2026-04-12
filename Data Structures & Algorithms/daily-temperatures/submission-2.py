class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        while stack is not empty and t is warmer than the temperature on top of the stack
        - let prev=stack.pop()
        - found the next warmer day for prev
        -set result[prev]=i-prev
        after finish popping on cooler days, push the current day 
        - stack.append(i)
        any days left in the stack at the end never get a warmer day --> stay 0 
        '''
        n=len(temperatures)
        result=[0]*n
        stack=[] #stores indices of days (monotonic decreasing by temperature)
        
        i=0
        while i<n: 
            #while current temp is warmer than the temp at the index on top of stack
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev=stack.pop()
                result[prev]= i-prev
            stack.append(i)
            i+=1
        return result