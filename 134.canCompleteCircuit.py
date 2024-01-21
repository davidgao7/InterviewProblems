# There are n gas stations along a circular route, where the amount of gas at
# the iᵗʰ station is gas[i].
#
#  You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from the iᵗʰ station to its next (i + 1)ᵗʰ station. You begin the journey
# with an empty tank at one of the gas stations.
#
#  Given two integer arrays gas and cost, return the starting gas station's
# index if you can travel around the circuit once in the clockwise direction,
# otherwise return -1. If there exists a solution, it is guaranteed to be unique
#
#
#  Example 1:
#
#
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4
#  = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to
# station 3.
# Therefore, return 3 as the starting index.
#
#
#  Example 2:
#
#
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to
# the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
#
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you
# only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.
#
#
#
#
#  Constraints:
#
#
#  n == gas.length == cost.length
#  1 <= n <= 10⁵
#  0 <= gas[i], cost[i] <= 10⁴
#
#
#  Related Topics Array Greedy 👍 11454 👎 1047
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_sum = 0
        total_sum = 0
        start = 0

        for i in range(len(gas)):
            current_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]

            # if current_sum < 0, then we can try start from the next start point
            # i从0开始累加rest[i]，和记为curSum，一旦curSum小于零，说明[0, i]区间都不能作为起始位置，
            # 因为这个区间选择任何一个位置作为起点，到i这里都会断油，那么起始位置从i+1算起，再从0计算curSum。
            if current_sum < 0:
                start = i + 1
                current_sum = 0

        # if total_sum < 0, then we can't find a start point to finish the circle
        if total_sum < 0:
            return -1

        return start

# leetcode submit region end(Prohibit modification and deletion)
