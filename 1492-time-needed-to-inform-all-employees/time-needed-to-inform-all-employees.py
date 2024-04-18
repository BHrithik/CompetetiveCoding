class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n==1:
            return informTime[0]
        employeeTree = defaultdict(lambda: [])
        for i in range(n):
            if i!= headID:
                employeeTree[manager[i]].append(i)
        print(employeeTree)
        Gtime = 0
        def dfs(managerId,time):
            nonlocal Gtime
            if not employeeTree[managerId]:
                Gtime = max(Gtime,time)
                return
            for i in employeeTree[managerId]:
                dfs(i,time+informTime[managerId])
        dfs(headID,0)
        return Gtime