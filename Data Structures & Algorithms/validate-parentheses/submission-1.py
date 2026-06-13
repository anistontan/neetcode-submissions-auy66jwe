class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={")":"(", "]":"[", "}":"{"}

        for c in s: 
            if c in closeToOpen: #check if its a closing parantheses
                if stack and stack[-1] == closeToOpen[c]: #use stack[-1] to get the top of stack
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)
        
        return True if not stack else False
        #return True if stack is empty