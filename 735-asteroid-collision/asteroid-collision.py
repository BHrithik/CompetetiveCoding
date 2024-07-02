class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if all(i>0 for i in asteroids) or all(i<0 for i in asteroids) or asteroids == [] or len(asteroids)==1:
            return asteroids
        for i in range(0,len(asteroids)-1):
            if i < len(asteroids):
                if asteroids[i] > 0 and asteroids[i+1] > 0:
                    continue
                if asteroids[i] <0 and asteroids[i+1] <0:
                    continue
                if asteroids[i] > 0 and asteroids[i+1] < 0:
                    if abs(asteroids[i]) > abs(asteroids[i+1]):
                        asteroids= asteroids[:i+1]+asteroids[i+2:]
                        return self.asteroidCollision(asteroids)
                    elif abs(asteroids[i]) < abs(asteroids[i+1]):
                        asteroids= asteroids[:i]+asteroids[i+1:]
                        return self.asteroidCollision(asteroids)
                    else:
                        asteroids= asteroids[:i]+asteroids[i+2:]
                        return self.asteroidCollision(asteroids)
        return asteroids