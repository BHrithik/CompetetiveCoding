class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        ll = []
        dl = []
        for i in logs:
            arr = i.split(" ")
            if arr[1][0].isalpha():
                ll.append(i)
            else:
                dl.append(i)
        ll.sort(key=lambda log: (log.split(maxsplit=1)[1], log.split(maxsplit=1)[0]))
        return ll+dl