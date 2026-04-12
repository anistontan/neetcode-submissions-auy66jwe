class Solution:
    def isValid(self, s: str) -> bool:
        '''
        make a mapping of closing --> opening: )-->(,]-->[, }-->{
        loop each char 
        - if its an opener, push 
        - if stack top!=matching opener : return false 
        - else pop 
        after loop: return stack is empty 
        '''
        stack=[]
        pairs = { ')':'(', ']':'[','}':'{'}

        for b in s: 
            if b in "([{":
                stack.append(b)
            else:
                if not stack: 
                    return False 
                if stack[-1]!=pairs[b]:
                    return False        
                stack.pop()
        return not stack #python shortcut, in python empty is treated as Fals, a non-empty list is True
        '''
        so if stack==[](empty) --> not stack is True --> return True
        so if stack!=[] (still has stuff) --> not stack is False --> return False 
        '''