from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if len(nums) == 2:
            return 0 if nums[0] == target else 1 if nums[1] == target else -1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target > nums[m]:
                # print("ola")
                l = m + 1  # eliminate half of the array
            elif target < nums[m]:
                # print("ola2")
                r = m - 1
            else:
                # print("hello")
                return m

        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    print(s.search(nums, target))
