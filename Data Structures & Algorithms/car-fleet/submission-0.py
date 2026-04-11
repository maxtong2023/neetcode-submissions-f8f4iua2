class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the positions of the cars in decreasing order. 

        cars = list(zip(position, speed)) # creates a tuple containing positions and speeds
        cars.sort(reverse = True) # sorts everything based on the first value of the tuple. (position)

        stack = []

        for car in cars: 
            time = (target - car[0]) / car[1]
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
            
