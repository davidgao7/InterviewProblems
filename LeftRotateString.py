# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        stack = []
        back = []
        
        for i in range(0,len(s)):
            if i>n-1:
                stack.append(s[i])
            else:
                back.append(s[i])
        
        new_s = ""
        for s in stack:
            new_s+=s
        for s in back:
            new_s+=s
        
        return new_s

