class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        #two stacks!
        '''
        self.stack = the normal stack (stores every value you push)
        self.min_stack = "minimum so far" stack (stores th emin at each level)
        '''

    def push(self, val: int) -> None:
        self.stack.append(val) #we push it into the normal stack 

        if not self.min_stack:#if min_stack is empty
            self.min_stack.append(val) #this is the first element ever
        else:#min_stack is not empty
            self.min_stack.append(min(val,self.min_stack[-1]))
            '''
            self.min_stack[-1] means: the current minimum (because top of min_stack stores the min so far)
            min(val, self.min_stack[-1]) picks the smaller one : 
            - either the new value val is the new minimum 
            - or the old minimum stays the minimum 
            then we append that result into min_stack
            '''

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
    
        
