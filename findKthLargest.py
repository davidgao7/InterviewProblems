# -*- coding:utf-8 -*-

class Solution:
    def findKth(self, a, n, K):
        # write code here
        # quick select

        # choosinig pivoit
        pivoit = n - 1

        # divide
        left = [x for x in a if x > a[pivoit]] # remember to use a[pivoit] instead of pivoit which is a index not actual number!
        mid = [x for x in a if x == a[pivoit]]
        right = [x for x in a if x < a[pivoit]] # find the largest first 从大到小

        l, m, r = len(left), len(mid), len(right)
        # if k in the left arr
        if K <= l:
            return self.findKth(left, l, K) # l only stand for length of left, not effect overall algorithm
        # if k on the right side
        elif K > l + m:
            return self.findKth(right, r, K - (l + m)) # r only stand for length of right, not effect overall algorithm
        # otherwise it means the mid # is the kth largest
        else:
            return mid[0]


s = Solution()
a, n, K = [10, 10, 9, 9, 8, 7, 5, 6, 4, 3, 4, 2], 12, 3
e = s.findKth(a, n, K)
print(e)
