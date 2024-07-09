class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # def count_fleets(target, position, speed):
    # Combine position and speed into a list of tuples and sort by position in descending order
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        current_time = 0
        
        # Iterate over the sorted list
        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            
            # If the current car's time to target is greater than the current fleet's time,
            # it means this car forms a new fleet.
            if time_to_target > current_time:
                fleets += 1
                current_time = time_to_target
        
        return fleets
