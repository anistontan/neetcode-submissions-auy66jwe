class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        - if the token is a number --> push it onto the stack 
        - if the token is an operator (+-*/) --> pop the top two numbers 
        -- b=pop() (most recent)
        -- a=pop()
        - compute a op b 
        -push the result back 
        --> at the end the stack has one value
        '''

        stack=[]

        for token in tokens:
            if token.lstrip('-').isdigit(): #so that it accepts negative too
                stack.append(int(token))
            else:
                b=stack.pop()
                a=stack.pop()

                if token=="+":
                    c=a+b
                elif token=="-":
                    c=a-b
                elif token=="*":
                    c=a*b
                elif token=="/":
                    c=int(a/b) #truncates towards 0
                 
                stack.append(c)

        return stack[-1]










        