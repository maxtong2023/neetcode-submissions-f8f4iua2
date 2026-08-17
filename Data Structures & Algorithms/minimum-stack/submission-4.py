class MinStack:

    def __init__(self):
        self.smallest = float('inf')
        self.stack = []


        

    def push(self, val: int) -> None:
        self.stack.append((val, self.smallest))
        self.smallest = min(self.smallest, val)
        

    def pop(self) -> None:
        # the tricky part is, when you pop the smallest value, how do you update it in constant time? 

        # you can maintain a list of the top two most small elements, but this gets weird if you have less than two. There are some conditionals that you would have to check. 

        # maintain a pointer to the second smallest element, and swap if rqeuired? Would need to maintain a set of numbers as well... 

        _, smallest_before_push = self.stack.pop()

        self.smallest = smallest_before_push
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.smallest
        
