class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_dict = Counter(moves)
        return move_dict['L'] == move_dict['R'] and move_dict['U'] == move_dict['D']