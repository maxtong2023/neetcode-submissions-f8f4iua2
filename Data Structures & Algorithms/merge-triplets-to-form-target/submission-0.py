class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #filter out the poison 

        result = [False, False, False]

        d,e,f = target

        for a, b, c in triplets: 
            if a <= d and b <= e and c <= f:
                if a == d:
                    result[0] = True
                if b == e:
                    result[1] = True
                if c == f:
                    result[2] = True
        if result == [True, True, True]:
            return True
        return False