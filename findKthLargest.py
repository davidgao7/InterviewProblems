# -*- coding:utf-8 -*-

class Solution:
    def findKth(self, a, n, K):
        # write code here
        # quick select
        left, right = 0, n - 1
        pivoit, a = self.partition(a, left, right)
        while pivoit != K - 1:
            if pivoit > K - 1:
                pivoit, a = self.partition(a, left, pivoit)
            elif pivoit < K - 1:
                pivoit, a = self.partition(a, pivoit + 1, right)

        return a[pivoit]

    def partition(self, a, left, right):
        pivoit = right
        index_pivoit = -1
        ref = []

        for i in range(left, right):
            if a[i] < a[pivoit]:
                ref.append(a[i])
                index_pivoit += 1
        for i in range(left, right):
            if a[i] == a[pivoit]:
                ref.append(a[i])
                index_pivoit += 1
        for i in range(left, right):
            if a[i] > a[pivoit]:
                ref.append(a[i])

        index_pivoit = index_pivoit + left
        return index_pivoit, ref


s = Solution()
a, n, K = [1332802,1177178,1514891,871248,753214,123866,1615405,328656,1540395,968891,1884022,252932,1034406,1455178,821713,486232,860175,1896237,852300,566715,1285209,1845742,883142,259266,520911,1844960,218188,1528217,332380,261485,1111670,16920,1249664,1199799,1959818,1546744,1904944,51047,1176397,190970,48715,349690,673887,1648782,1010556,1165786,937247,986578,798663],49,24
e = s.findKth(a, n, K)
print(e)
