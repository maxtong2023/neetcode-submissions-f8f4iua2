class Solution:
    def checkValidString(self, s: str) -> bool:
        # retain a stack. If the stack has (, pop off if there is an 
        # element * or ). if the stack is empty and you find ), return 
        # false, if *, do nothing.

        # the current implementation fails because there may be cases 
        # in which ) exists at the end but we popped it all because 
         # we found *

        # my thinking is that we can keep a count of * that we COULD HAVE
        # used to pop a ( off, and subtract that at the end.

        # ok so i cant read. 

        # need to find a way to pass (*))

        high = 0 
        low = 0 

        for i in s: 
            if i == '(':
                high += 1
                low += 1
            elif i == ')':
                low -=1
                high -=1
            else:
                low -= 1
                high += 1
            if high < 0: 
                return False
            if low < 0: 
                low = 0
        return low ==0
            

                
            
