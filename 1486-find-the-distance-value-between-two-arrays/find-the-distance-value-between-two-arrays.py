class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # n = len(arr1)
        count = 0
        for num1 in arr1:
            if all(abs(num1 - num2) > d for num2 in arr2):
                count += 1
        return count
        # n2 = len(arr2)
        # mini = min(arr2)
        # maxi = max(arr2)
        # non_negative_elements = [i for i in arr2 if i >= 0]
        # negative_elements = [i for i in arr2 if i < 0]
        # if non_negative_elements:
        #     mini2 = min(non_negative_elements)
        # else:
        #     mini2 = float('-inf')
        # if negative_elements:
        #     maxi2 = max(negative_elements)     
        # else:
        #     maxi2 = float('-inf')
        # print(mini)
        # print(maxi)
        # print(mini2)
        # print(maxi2)
        # for i in range(n):
        #     if abs(arr1[i] - mini) > d and abs(arr1[i] - maxi) > d and abs(arr1[i] - mini2) > d and abs(arr1[i] - maxi2) > d:
        #         count += 1
        # return count