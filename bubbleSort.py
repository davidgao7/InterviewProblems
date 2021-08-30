class BubbleSort():
    """docstring for BubbleSort."""

    def __init__(self, arr):
        super(BubbleSort, self).__init__()
        # self.arr = arr # shallow copy, the origin will change also:                                                           (base) tengjungao@Tengjuns-MacBook-Pro InterviewProblems % python3 bubbleSort.py
                                                                                                                                # origin: [3, 3, 4, 4, 6, 7]
                                                                                                                                # sorted: [3, 3, 4, 4, 6, 7]
        # for deep copy
        self.arr = []
        for e in arr:
            self.arr.append(e) # need to construct new arr obj(deep copy)                                                       (base) tengjungao@Tengjuns-MacBook-Pro InterviewProblems % python3 bubbleSort.py
                                                                                                                                # origin: [3, 4, 7, 3, 4, 6]
                                                                                                                                # sorted: [3, 3, 4, 4, 6, 7]


    def swap(self, i, j):
        swp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = swp

    def sort_e(self, index):
        # bubble up
        idx = index
        for i in range(idx-1,0,-1):
            if self.arr[i] > self.arr[idx]:
                self.swap(i, idx)
                idx = i # update value index

    def sort(self):
        for i in range(0, len(self.arr)):
            self.sort_e(i)
        return self.arr


arr = [3,4,7,3,4,6]
print("origin: %s\n" % arr)
sorting = BubbleSort(arr)
arr_sort = sorting.sort()
print("sorted: %s" % arr_sort)
