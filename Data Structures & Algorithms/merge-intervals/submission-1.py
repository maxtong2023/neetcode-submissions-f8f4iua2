class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals: 
            return []
        
        intervals = sorted(intervals)
        result = [intervals[0]] # always start woth the first interval

        for i in range(1, len(intervals), 1):
            n = len(result) - 1

            if intervals[i][0] <= result[n][1]: # need to merge: 
                result[n][0] = min(result[n][0], intervals[i][0])
                result[n][1] = max(result[n][1], intervals[i][1])
            else:
                result.append(intervals[i])
        return result

