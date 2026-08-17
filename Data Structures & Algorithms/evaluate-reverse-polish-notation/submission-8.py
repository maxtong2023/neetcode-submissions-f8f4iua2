class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": "",
            "-": "",
            "*": "",
            "/": ""
        }

        stack = []
        result = 0
        

        for token in tokens: 
            # i think i can always assume that there are going to be 2
            # elements in the stack when there is an operator. 
            if token in operators: 
                num1 = int(stack.pop())
                num2 = int(stack.pop())

                if token == "+": 
                    result = num2 + num1
                    stack.append(result)
                elif token == "-": 
                    result = num2 - num1
                    stack.append(result)
                elif token == "*": 
                    result = num2 * num1
                    stack.append(result)
                else: 
                    result = int(num2 / num1) 
                    stack.append(result)
            else: 
                stack.append(token)
        return int(stack.pop())