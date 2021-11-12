//
// Created by Tengjun Gao on 11/12/21.
//
#include "vector"
#include "iostream"

using namespace std;

class Solution {
public:
    void printVector(vector<int> answer) {
        printf("[");
        for (int i = 0; i < answer.size(); i++) {
            if (i != answer.size() - 1) {
                printf("%d,", answer[i]);
            } else {
                printf("%d", answer[i]);
            }
        }
        printf("]");
    }

    vector<int> searchRange(vector<int> &nums, int target) {
        //找到目标的开始位置和结束位置
        if (nums.size() == 1 && nums[0] == target) { return vector<int>{0, 0}; }
        vector<int> answer;
        if (nums.size() == 2) {
            if (nums[0] == target) { answer.push_back(0); }
            if (nums[1] == target) { answer.push_back(1); }
            if (nums[0] != target && nums[2] != target) {
                answer.push_back(-1);
                answer.push_back(-1);
            }
            return answer;
        }

        int left = 0, right = nums.size() - 1, mid = (left + right) >> 1;
        while (left < right) {
            int val = nums[mid];

            if (val == target) {
                if (answer.empty()) {
                    answer.push_back(mid);
                }
                if (!answer.empty() && answer.back() != mid) {
                    answer.push_back(mid);
                }
                left++;
            } else if (val < target) {
                left++;
            } else if (val > target) {
                right--;
            }

            mid = (left + right) >> 1;
//            printf("left=%d , right=%d, mid=%d\n", left, right, mid);
        }
        if (answer.empty()) {
            answer.push_back(-1);
            answer.push_back(-1);
        }
        return answer;
    }
};

int main() {
    Solution *s = new Solution();
    vector<int> nums = {1,2,3};
    int target = 0;
    vector<int> answer = s->searchRange(nums, target);
    s->printVector(answer);
}