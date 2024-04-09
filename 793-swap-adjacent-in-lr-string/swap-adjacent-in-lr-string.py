class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end): return False
        if start.replace('X','') != end.replace('X',''): return False
        LsInStart = [ x for x in range(len(start)) if start[x] == 'L']
        RsInStart = [ x for x in range(len(start)) if start[x] == 'R']
        LsInEnd = [ x for x in range(len(end)) if end[x] == 'L']
        RsInEnd = [ x for x in range(len(end)) if end[x] == 'R']

        for i,j in zip(LsInStart,LsInEnd):
            if i < j:
                return False
        
        for i,j in zip(RsInStart,RsInEnd):
            if i > j:
                return False
        
        return True