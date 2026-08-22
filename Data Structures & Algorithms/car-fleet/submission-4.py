import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0

        # my idea is that you can calculate how long it takes for the car to get to the end.

        # for example in example 2, position 4 takes 3 units of time to reach the destination, and position 7 also takes 3 units of time. 

        # because position 4 is before position 7 and it takes less than or equal to time to reach the destination, it must form a fleet. 

        times = []
        zipped = list(zip(position, speed))
        zipped.sort()

        for pos, vel in zipped: 
            time = (target - pos) /vel
            times.append(time)

        # now, loop through, find all the instances in which there is an element less than or equal to an element in the future. In which case there will be a fleet. 
        stack =[]
        fleets = len(position)
        for time in times: 
            while stack and time >= stack[-1]: 
                stack.pop()
                fleets -= 1
            stack.append(time)
        return fleets


