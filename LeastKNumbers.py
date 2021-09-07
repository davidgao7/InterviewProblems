# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        left, right = 0, len(tinput) - 1
        answer = []
        if len(tinput) == 0 or k == 0:
            return []
        piviot, tinput = self.partition(tinput, left, right)
        if piviot > k - 1:
            answer.append(self.GetLeastNumbers_Solution(tinput[:piviot], k))
        if piviot < k - 1:
            answer.append(tinput[piviot:])
            answer.append(self.GetLeastNumbers_Solution(tinput[:piviot], k - piviot))
        if piviot == k - 1:
            answer.append(tinput[:piviot + 1])  # include pivot
        answer = [item for sublist in answer for item in sublist]  # flatten the list
        return answer

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
        return index, result


s = Solution()
# n1 = 4
# test1 = [4, 5, 1, 6, 2, 7, 3, 8]
# result1 = s.GetLeastNumbers_Solution(test1, n1)
# print(result1)
# test2 = [1]
# n2 = 0
# result2 = s.GetLeastNumbers_Solution(test2, n2)
# print(result2)
test3 = [0, 1, 2, 1, 2]
n3 = 3
result3 = s.GetLeastNumbers_Solution(test3, n3)
print(result3)
# test4 = [234,233,233,233,233,233,233,233,233,233,233,233,233,233,233,233,233,233,233,233]
# n4 = 10
# result4 = s.GetLeastNumbers_Solution(test4, n4)
# print(result4)