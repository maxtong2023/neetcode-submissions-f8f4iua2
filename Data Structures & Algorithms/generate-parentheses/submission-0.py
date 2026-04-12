class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # maybe a naive way is to backtrack every possible subset
        # remove all duplicates by including a set, and only appending 
        # if it is a valid parantheses

        result = []
        

        def backtrack(path, opens, closes): 
            if closes > opens: 
                return 

            if len(path) == n * 2: 
                result.append("".join(path))
                
            if opens < n: 
                path.append("(")
                backtrack(path, opens +1, closes)
                path.pop()
            if closes < n: 
                path.append(")")
                backtrack(path, opens, closes + 1 )
                path.pop()
        backtrack([], 0, 0)
        return result


