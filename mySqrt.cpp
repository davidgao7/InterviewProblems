//Given a non-negative integer x, compute and return the square root of x.
//
// Since the return type is an integer, the decimal digits are truncated, and
//only the integer part of the result is returned.
//
// Note: You are not allowed to use any built-in exponent function or operator,
//such as pow(x, 0.5) or x ** 0.5.
//
//
// Example 1:
//
//
//Input: x = 4
//Output: 2
//
//
// Example 2:
//
//
//Input: x = 8
//Output: 2
//Explanation: The square root of 8 is 2.82842..., and since the decimal part
//is truncated, 2 is returned.
//
//
// Constraints:
//
//
// 0 <= x <= 2³¹ - 1
//
// Related Topics 数学 二分查找 👍 824 👎 0

#include "iostream"
#include "vector"

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int mySqrt(int x) {
        // 二分查找
        int l = 0, r = x, ans = -1; // 平方根取值下限0， 上限x

        while (l <= r) { // 缩小范围
            int mid = l + (r - l) / 2;
            if ((long long) mid * mid <= x) { //值大了往左缩，小了往右缩
                ans = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return ans;
    }
};
//leetcode submit region end(Prohibit modification and deletion)

int main() {
    Solution *s = new Solution();
    int a = 7;
    cout << "sqrt of " << a << " is " << s->mySqrt(a) << endl;
}