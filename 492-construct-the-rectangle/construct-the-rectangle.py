class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l,w = 0, 0
        for i in range(1,int(area**0.5)+1):
            if area%i == 0:
                if i <= area/i:
                    l = int(area/i)
                    w = i
        return [l,w]