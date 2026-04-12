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

        #sort by position, biggest first (closest to target first)
        cars.sort(reverse=True)

        stack=[] #stores fleet arrival times

        for pos,spd in cars:
            time=(target-pos)/spd #for each car compute its time to reach target
            stack.append(time)

            #if this car catches the fleet in front, merge (same fleet)
            #(<= includes"meets exactly at the destination" case)

            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        
        return len(stack)