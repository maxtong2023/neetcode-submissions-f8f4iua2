class TimeMap:

    def __init__(self):
        self.timeset = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.timeset.get(key): 
            self.timeset[key] = []
            self.timeset[key].append((value, timestamp))
        else:
            self.timeset[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeset: 
            return ""
        left = 0 
        right = len(self.timeset[key]) - 1
        result = ""
        while left <= right: 
            mid = (left + right) // 2

            stamp = self.timeset[key][mid][1]

            if stamp <= timestamp: 
                result = self.timeset[key][mid][0] # 0 is the value
                left = mid + 1
            else:
                right = mid - 1 
        return result
        
