class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = [int(i[11:14]) for i in details if int(i[11:13]) > 60]
        return len(seniors)