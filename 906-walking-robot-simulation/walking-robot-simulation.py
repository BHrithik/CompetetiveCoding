class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple,obstacles))
        def obstacleInPath(X, Y, dx, dy, distance):
                for step in range(distance):
                    if (X + dx, Y + dy) not in obstacle_set:
                        X += dx
                        Y += dy
                    else:
                        break
                return [X, Y]

        X = 0
        Y = 0
        direction = 0 # 0- N 1-E 2-S 3-W 
        turnLeft = {0:3, 1:0, 2:1, 3:2}
        turnRight = {0:1, 1:2, 2:3, 3:0}
        res = float('-inf')
        for command in commands:
            if command >0:
                # Check obstacle
                if direction == 0:  # North
                    X, Y = obstacleInPath(X, Y, 0, 1, command)
                elif direction == 1:  # East
                    X, Y = obstacleInPath(X, Y, 1, 0, command)
                elif direction == 2:  # South
                    X, Y = obstacleInPath(X, Y, 0, -1, command)
                elif direction == 3:  # West
                    X, Y = obstacleInPath(X, Y, -1, 0, command)
                res = max(res, (X**2+Y**2))
            else:
                if command == -1:
                    direction = turnRight[direction]
                if command == -2:
                    direction = turnLeft[direction]
        return res