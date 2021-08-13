# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        # 在数组中查找两个数，使得他们的和正好是S，
        # 如果有多对数字的和等于S，返回两个数的乘积最小的，如果无法找出这样的数字，返回一个空数组即可。
        if array == []: return []
        idx = []
        product = []
        min_idx = 0
        product_idx = 0
        for i in range(len(array)):
            for j in range(i+1, len(array)):
                if array[i] + array[j] == tsum:
                    idx.append([i,j])
                    product.append(array[i]*array[j])
                    if product[product_idx-1] > product[product_idx]:
                        min_idx = product_idx
                        product_idx+=1
        if idx == []: return [] # base case
        return [array[idx[min_idx][0]],array[idx[min_idx][1]]] # return number
