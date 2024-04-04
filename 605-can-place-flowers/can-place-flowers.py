class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
        for i in range(0,len(flowerbed)):
            if i-1 >= 0 and i+1 < len(flowerbed) and flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n = n-1
                flowerbed[i] = 1
            if i == 0 and i+1 < len(flowerbed) and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                n = n-1
                flowerbed[i] = 1
            if i == len(flowerbed)-1 and i-1 >= 0 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                n = n-1
                flowerbed[i] = 1
        if n <= 0:
            return True
        else:
            return False
        
        