class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = list(zip(heights,names))
        ans.sort()
        return [i[1] for i in ans[::-1]]