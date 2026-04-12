class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        a car cannot pass a car infront 
        so if a car behind is faster, it can :
        - catch up to the car ahead
        - must slow down and follow aat the same speed 
        - from that point on, they move together
        RETURN how many separate fleets arrive at a target 
        fleet : one or more cars that end up arriving together
        '''
        cars=[]
        for i in range(len(position)):
            cars.append((position[i],speed[i]))

        cars.sort(reverse=True)

        stack=[]

        for pos,spd in cars:
            time=(target-pos)/spd
            stack.append(time)

            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        
        return len(stack)