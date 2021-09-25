#
# max sum of the subarray
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxsumofSubarray(self , arr ):
        # write code here
        ans_max = arr[0]
        # 从下一个开始
        for i in range(1, len(arr)):
            # 从前往后推，要保证每个位置的值都起码比原本的大。注意每次都要用m保存当前时刻的最大累积和，最后直接返回就ok。
            print(arr)
            print("\n")
            print("arr[%d] = %d compare with arr[%d]+arr[%d] = %d + %d = %d\n" % (i, arr[i], i-1, i, arr[i-1], arr[i], arr[i-1]+arr[i]))
            arr[i] = max(arr[i], arr[i-1]+arr[i])
            print("get arr[%d] = %d\n" % (i, arr[i]))
            ans_max = max(ans_max, arr[i])
            print("ans_max = %d compare with %d, get %d\n" % (ans_max, arr[i], ans_max))
            print("======================================================================")
        return ans_max

s = Solution()
arr = [1, -2, 3, 5, -2, 6, -1]
ans = s.maxsumofSubarray(arr)
print("final answer: %d\n" % ans)