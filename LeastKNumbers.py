# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        answer = [-1] * len(tinput)
        left, right = 0, len(tinput) - 1
        number = 0

        while (number < k):
            piviot = self.partition(tinput, left, right)
            if piviot <= k:
                answer[piviot] = tinput[-1]
                number += 1
            else:
                right = piviot - 1

        return answer[k:]

    def partition(self, tinput, left, right):
        piviot = right
        result = [tinput[piviot]]
        index = 0
        for i in range(left, piviot):
            if tinput[i] <= tinput[piviot]:
                result.insert(0, tinput[i])
                index += 1
            else:
                result.append(tinput[i])
        return index

    def swap(self, i, j, arr):
        swp = arr[i]
        arr[i] = arr[j]
        arr[j] = swp


test1 = [4, 5, 1, 6, 2, 7, 3, 8]
n = 4
s = Solution()
result = s.GetLeastNumbers_Solution(test1, n)
print(result)
