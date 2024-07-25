class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        left_sorted_array = self.sortArray(left)
        right_sorted_array = self.sortArray(right)
        return self.MergeArray(left_sorted_array,right_sorted_array)
    
    def MergeArray(self, arr1:List[int], arr2: List[int]) -> List[int]:
        i,j = 0, 0
        res = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i = i+1
            else:
                res.append(arr2[j])
                j = j+1
        res.extend(arr1[i:])
        res.extend(arr2[j:])
        return res