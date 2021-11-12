//
// Created by Tengjun Gao on 11/12/21.
//
#include "vector"
#include "iostream"

using namespace std;

class Solution {
public:
    int searchInsert(vector<int> &nums, int target) {
        int n = nums.size();
        int left=0, right = n-1, ans = n;

        while(left <= right){
            int mid = ((right - left) >> 1) + left; // right shift <==> // 2

            if (target <= nums[mid]){
                ans = mid;
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return ans;
    }
};

int main() {
    Solution *s = new Solution();
    vector<int> nums = {1,3,5,6};
    int target = 2;
    cout << "position of " << target << " in " << "{1,3,5,6} is " << s->searchInsert(nums, target) << endl;
}