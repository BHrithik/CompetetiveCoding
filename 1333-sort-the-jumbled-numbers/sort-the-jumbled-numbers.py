class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convertToMappedVal(num,mapDict):
            num = str(num)
            val = 0
            for i in num:
                val = val*10 + mapDict[int(i)]
            return val
        mapDict = defaultdict()
        # mapping = [str(i) for i in mapping]
        for i in range(len(mapping)):
            mapDict[i] = mapping[i]
        new_list = []
        for i in range(0,len(nums)):
            new_list.append((convertToMappedVal(nums[i],mapDict),i,nums[i]))
        new_list.sort()
        print(new_list)
        return [i[2] for i in new_list]
