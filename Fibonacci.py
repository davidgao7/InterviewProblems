#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def Fibonacci(self , n ):
        # write code here
        s = [0,1]
        for i in range(0,n+1):
            if i != 0 and i!=1:
                if s[-1] + s[-2] > 1000000007:
                    s[-1] = 1
                    break
                s.append(s[-1]+s[-2])
                i+=1
            else:
                i+=1
        return s[-1]


s = Solution()
print(s.Fibonacci(5))
a = "abc\"ab"
print(a)