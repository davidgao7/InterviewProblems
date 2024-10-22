import heapq
from collections import Counter

"""
python heapq lib

import heapq

heap properties:
    - min heap : parent <= children
    - max heap : parent >= children

can also be used as priority queue
can also use to sort key value pairs, sort by key

heapq : min heap

methods:

    - heapq.heapify(list) : convert list to a min heap, time complexity O(n), space complexity O(1)
    - heapq.heappush(heap, item) : insert item into heap, time complexity O(logn), space complexity O(1)
    - heapq.heappop(heap) : remove and return smallest element from heap, time complexity O(logn), space complexity O(1)
    - heapq.heappushpop(heap, item) : push item onto heap, then pop and return smallest element, O(logn), space complexity O(1)
    - heapq.heapreplace(heap, item) : pop and return smallest element, then push item, O(logn), space complexity O(1)

simple example:

    - heap sort: convert list to heap, then pop elements from heap, time complexity O(nlogn), space complexity O(n)
    - put tuple into heap, sort by key
"""

"""
python Counter lib

from collections import Counter

a_list = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1]

counter = Counter(a_list)

counter
Counter({1: 8, 2: 3, 3: 2, 4: 1, 5: 1})

then we can use heapq to sort the counter by value(frequency) or key

heapq.heapify(list(counter.items()))
"""

a_list = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1]
print(a_list)

counter = Counter(a_list)

print(counter)


res = list(counter.items())
print("before heapify")
print(res)
heapq.heapify(res)
print("after heapify, sort by key, min heap")
print(res)

print("sort by frequency (freqnency, value), min heap")
frequency_heap = []
for val, freq in res:
    heapq.heappush(frequency_heap, (freq, val))
    print(f"current smallest element sort by freqency: {frequency_heap[0]}")

res = []
while frequency_heap:
    res.append(heapq.heappop(frequency_heap))
print(f"res sort by frequency, (freqency, val): {res}")

print("=========================")
# we can also use heapify to sort the list, time complexity O(n), space complexity O(n)
res = list(counter.items())
print("before heapify: ", res)
# turn list into min heap
heapq.heapify(res)
print("sort by key, min heap: ", res)

print("get current smallest frequency in min heap right after inserting an element")
min_heap = []
for e, freq in counter.items():
    # heappushpop() is equivalent to heappush() followed by heappop()
    # so it will push the new element into heap, then pop the smallest element
    print(f"current elements: {min_heap}")
    print(heapq.heappushpop(min_heap, (freq, e)))  # sort by key

print("=========================")
# heapreplace is equivalent to heappop() followed by heappush()
# Pop and return the current smallest value, and add the new item.
a = [2, 7, 4, 0, 8, 12, 14, 13, 10, 3, 4]
print(a)
b = a[:]
heapq.heapify(a)
heapq.heapify(b)
print(
    f"popping smallest element after pushing -1: {heapq.heappushpop(a, -1)}"
)  # equal to heappop() then heappush()
print(
    f"popping smallest element before pushing -1: {heapq.heapreplace(b, -1)}"
)  # more efficient than heappushpop(), does not change size of heap
print(f"list after pushing -1 and pop smallest: {a}")
print(f"list pop the smallest element, then push -1: {b}")


print("=========================")
# heapq.merge: merge multiple sorted iterables into a single sorted output
array1 = [1, 3, 5]
array2 = [2, 4, 6]
array3 = [0, 7, 8]
merged = heapq.merge(array1, array2, array3)
# Convert to list for display purposes
merged_list = list(merged)
print(merged_list)

array1 = [(1, "a"), (3, "c"), (5, "e")]
array2 = [(2, "b"), (4, "d"), (6, "f")]
array3 = [(0, "z"), (7, "g"), (8, "h")]
merged = heapq.merge(
    array1, array2, array3
)  # merge the iterables into 1 interable and sort by key
# Convert to list for display purposes
merged_list = list(merged)
print(merged_list)

print("=========================")
# heapq.nlargest(n, iterable, key=None) : return n largest elements in iterable, time complexity O(nlogn), space complexity O(n)
# heapq.nsmallest(n, iterable, key=None) : return n smallest elements in iterable, time complexity O(nlogn), space complexity O(n)
nums = [1, 1, 3, 2, 5, 2, 7, 8, 5, 3, 2]
print(nums)
n = 2
print(
    f"{n} Largest from high to low:",
    heapq.nlargest(n, nums),
    type(heapq.nlargest(n, nums)),
)  # get first larget, then second largest etc...
print(
    f"{n} Smallest from low to high:",
    heapq.nsmallest(n, nums),
    type(heapq.nsmallest(n, nums)),
)  # get first smallest, then second smallest etc...

print("\nsort by key(freqency in Counter)")
counter = Counter(nums)
print(
    "counter(element, frequency): ", counter.items()
)  # already sorted by key(element)
print(
    f"{n} Largest from high to low, sort by freqency:",
    heapq.nlargest(n, nums, key=lambda x: counter[x]),
    type(heapq.nlargest(n, nums)),
)  # get first larget, then second largest etc...
print(
    f"{n} Smallest from low to high, sort by freqency:",
    heapq.nsmallest(n, nums, key=lambda x: counter[x]),
    type(heapq.nsmallest(n, nums)),
)
