# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        ans = []
        for i in range(k):
            ans.append(self.quick_select(tinput, i))
        return ans

    def quick_select(self, tinput, i):
        pivot = len(tinput) - 1
        j = 0

        while pivot != i:
            if tinput[j] <= tinput[pivot] and j < pivot:  # all left is less than pivot
                j += 1
            else:
                self.swap(tinput, pivot, j)
                if j == pivot:
                    pivot -= 1
                    j = 0  # swap next largest val

        return tinput[pivot]

    def swap(self, arr, i, j):
        swp = arr[i]
        arr[i] = arr[j]
        arr[j] = swp


s = Solution()
input = [0, 0, 2, 0, 4, 2, 4, 0, 7, 3, 2, 10, 7, 9, 10, 4, 1, 4, 2, 10, 3, 16, 8, 22,
         18, 10, 6, 16, 8, 2, 28, 24, 24, 27, 2, 28, 34, 35, 7, 29, 31, 16, 25, 9,
         0, 21, 38, 33, 16, 11, 2, 16, 37, 28, 19, 45, 29, 8, 2, 26, 24, 12, 36, 29,
         31, 40, 10, 59, 20, 64, 60, 45, 4, 40, 49, 66, 59, 64, 66, 70, 76, 16, 18, 8,
         73, 66, 46, 63, 67, 43, 3, 75, 33, 46, 80, 51, 75, 84, 6, 96, 33, 12, 60, 52, 62,
         84, 100, 39, 64, 74, 87, 25, 61, 37, 21, 40, 44, 87, 2, 23, 3, 116, 6, 122, 71, 1, 66, 75,
         110, 87, 103, 44, 109, 81, 82, 25, 133, 4, 85, 45, 34, 111, 57, 53, 41, 62, 29, 94, 125, 4, 54,
         95, 88, 136, 61, 15, 121, 15, 144, 132, 14, 136, 103, 34, 158, 134, 121, 15, 136, 56, 128, 95, 133, 25, 91,
         168, 4, 88, 137,
         143, 23, 111, 93,
         139, 182, 81, 105, 60, 93, 39, 37, 91, 186, 138, 162, 58, 105, 125, 144, 171, 122, 30, 143, 32, 132, 123, 57,
         31, 188, 150, 91
    , 1, 190, 57, 86,
         166, 3, 77, 145, 48, 86, 189, 79, 204, 147, 124, 207, 3, 138, 17, 37, 212, 192, 137, 51, 188, 85, 63, 144, 210,
         9, 187, 62, 74, 131,
         49, 176, 190,
         134, 215, 215, 143, 22, 219, 116, 199, 43, 19, 149, 106, 186, 84, 257, 167, 69, 26, 207, 91, 11, 154, 128, 206,
         65, 184, 207, 165, 225, 218,
         196,
         199, 190, 134, 238, 268, 34, 270, 70, 166, 128, 121, 180, 50, 259, 64, 7, 100, 167, 8, 208, 96, 73, 140, 158,
         109, 245,
         40, 118, 164, 42, 221, 171,
         20, 261, 229, 230, 295, 190, 151, 130, 286, 82, 103, 117, 148, 180, 15, 55, 111, 58, 247, 277, 76, 317, 13,
         326, 78, 138, 207
    , 95, 54, 273, 185, 21,
         250, 24, 327, 48, 345, 160, 253, 132, 345, 71, 150, 51, 187, 11, 237, 51, 130, 286, 126, 220, 224, 227, 192,
         113, 268,
         20, 20, 357, 37, 153, 41, 217,
         12, 8, 153, 314, 288, 217, 304, 88, 230, 238, 16, 9, 248, 375, 350, 27, 70, 156, 108, 384, 73, 213, 245, 385,
         252, 83, 188,
         201, 64, 65, 290, 370, 48,
         21, 116, 390, 149, 71, 36, 190, 186, 126, 249, 90, 191, 238, 82, 26, 387, 345, 318, 226, 58, 134, 283, 320, 90,
         28, 318, 356, 257, 244, 219, 417, 116, 195, 77, 199, 172, 408, 297, 37, 270, 435, 342, 171, 339, 80, 36, 233,
         85,
         264, 153, 354, 95, 309, 62, 347, 173, 152, 348, 372, 322, 268, 261, 104, 197, 370, 90, 181, 76, 428, 296, 354,
         136, 83, 138, 169, 195, 375, 121, 59, 376, 3, 294, 328, 401, 135, 470, 50, 103, 383, 30, 3, 436, 11, 101, 188,
         218, 138, 135, 125, 296, 229, 451, 342, 328, 29, 254, 366, 507, 68, 339, 260, 69, 468, 49, 84, 132, 509, 473,
         65, 127, 226, 321, 110, 33, 367, 452, 340, 449, 508, 324, 237, 21, 367, 80, 356, 262, 24, 253, 335, 60, 88, 11,
         471,
         73, 42, 403, 349, 19, 72, 150, 231, 343, 311, 243, 362, 465, 191, 267, 341, 429, 399, 411, 272, 145, 267, 507,
         501, 140, 496,
         227, 236, 39, 56, 472, 151, 3]
k = 58
print(s.GetLeastNumbers_Solution(tinput=input, k=k))
