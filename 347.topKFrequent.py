# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
#
#  Example 1:
#  Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
#  Example 2:
#  Input: nums = [1], k = 1
# Output: [1]
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁵
#  -10⁴ <= nums[i] <= 10⁴
#  k is in the range [1, the number of unique elements in the array].
#  It is guaranteed that the answer is unique.
#
#
#
#  Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
#
#  Related Topics Array Hash Table Divide and Conquer Sorting Heap (Priority
# Queue) Bucket Sort Counting Quickselect 👍 16425 👎 601

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq  # min heap

        # 时间复杂度：O(nlogk)
        # 空间复杂度：O(n)

        # 要统计元素出现频率
        map_ = {}  # nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        # 对频率排序
        # 定义一个小顶堆，大小为k
        pri_que = []  # 小顶堆

        # 用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:  # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)

        # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        """
        find the k most frequent elements
        :param nums:
        :param k:
        :return:
        """
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for key, v in count.items():
            freq[v].append(key)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    s = Solution()
    print(s.topKFrequent(nums, k))
    print(s.topKFrequent2(nums, k))
