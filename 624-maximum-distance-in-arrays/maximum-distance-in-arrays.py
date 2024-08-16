class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min,cur_max = arrays[0][0], arrays[0][-1]
        res = 0
        for arr in arrays[1:]:
            res = max(res,
            cur_max-arr[0],arr[-1]-cur_min
            )
            cur_max = max(arr[-1],cur_max)
            cur_min = min(cur_min,arr[0])
        return res
        # max_array = sorted(arrays, key=lambda x: max(x))
        # min_array = sorted(arrays, key=lambda x: min(x))
        # max_value1 = max_array[-1][-1]
        # max_value2 = max_array[-2][-1]
        # min_value1 = min_array[0][0]
        # min_value2 = min_array[1][0]
        # if max_array[-1] == min_array[0]:
        #     return max(max_value1 - min_value2, max_value2 - min_value1)
        # else:
        #     return max_value1 - min_value1
        # return 0