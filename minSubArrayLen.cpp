//给定一个含有 n 个正整数的数组和一个正整数 target 。
//
// 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长
//度。如果不存在符合条件的子数组，返回 0 。
//
//
//
// 示例 1：
//
//
//输入：target = 7, nums = [2,3,1,2,4,3]
//输出：2
//解释：子数组 [4,3] 是该条件下的长度最小的子数组。
//
//
// 示例 2：
//
//
//输入：target = 4, nums = [1,4,4]
//输出：1
//
//
// 示例 3：
//
//
//输入：target = 11, nums = [1,1,1,1,1,1,1,1]
//输出：0
//
//
//
//
// 提示：
//
//
// 1 <= target <= 10⁹
// 1 <= nums.length <= 10⁵
// 1 <= nums[i] <= 10⁵
//
//
//
//
// 进阶：
//
//
// 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
//
// Related Topics 数组 二分查找 前缀和 滑动窗口 👍 822 👎 0
#include <iostream>
#include <vector>
#include <math.h>
#include <sstream>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    // 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长
    // 度。如果不存在符合条件的子数组，返回 0 。
    int minSubArrayLen(int target, vector<int> &nums) {
        // 滑动窗口： T:O(n), S:O(1)
        int result = INT32_MAX;
        int i = 0, j = 0;
        int sum = 0;
        if (nums.size() == 0) return 0;

        while (j < nums.size()) {
            sum += nums[j];
            while (sum >= target) { // 达到要求后，向右移动起点，寻找下一个和>=target的subarray，并每一次记录出最短的array
                result = min(result, j - i + 1);
                sum -= nums[i]; //去掉第一个，让下一个当新的头
                i++;
            }
            j++; // 如果没达到要求或从新开始找新subarray，轮下一个元素
        }
        return result == INT32_MAX ? 0 : result; // 如果不幸while没运行，return 0
    }

    int minSubArrayLen2(int target, vector<int> &nums) {
        // 二分查找： T:O(nlogn), S:O(n)
        // precondition: every element in nums needs to be (+)
        if (nums.size() == 0) return 0;

        int ans = INT_MAX;
        vector<int> sums(nums.size()+1, 0);
        // sums[0] ==> 前 0 个元素的和为0

        for (int i = 1; i<nums.size(); i++){
            target = target + sums[i-1];
            //lower_bound Returns an iterator pointing to the first element in the range [first, last) that is not less than (i.e. greater or equal to) value, or last if no such element is found.
            //实现这里二分查找大于等于某个数的第一个位置的功能
            auto bound = lower_bound(sums.begin(), sums.end(),target);

            if (bound != sums.end()){
                int b = static_cast<int>((bound-sums.begin())-(i-1));
                ans = min(ans, b);
            }
        }
        return ans == INT_MAX ? 0 : ans;
    }
};

//leetcode submit region end(Prohibit modification and deletion)
int main() {
    vector<int> nums = {1, 2, 3, 4, 5};
    int target = 11;

    stringstream ss;
    string str;
    copy(nums.begin(), nums.end(), ostream_iterator<int>(ss, ","));
    printf("array: [%s], target = %d\n", ss.str().c_str(), target);

    Solution *s = new Solution();
    int ans1 = s->minSubArrayLen(target, nums);
    int ans2 = s->minSubArrayLen2(target, nums);

    cout << ans1 << endl;
    cout << ans2 << endl;
}