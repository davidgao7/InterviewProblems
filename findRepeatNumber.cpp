//
// Created by Tengjun Gao on 10/8/21.
//
using namespace std;

#include "vector"
#include "set"

class Solution {
public:
    int findRepeatNumber(vector<int> &nums) { // 请找出数组中任意一个重复的数字。
        set<int> *num_set = new set<int>;

        for (int num:nums) {
            if (!num_set->count(num)){ // more than 1, but should only at most 1 in this case
                num_set->insert(num);
            }else{
                return num;
            }
        }
        return -1;
    }
};

int main() {
    Solution *solution = new Solution();
    vector<int> input = {2, 3, 1, 0, 2, 5, 3};
    int answer = solution->findRepeatNumber(input); // pass in the memory location of the array/list/vector
    printf("%d",answer);

//    提交结果	执行用时	内存消耗	语言	提交时间	备注
//    通过
//    48 ms	27.1 MB	C++	2021/10/08 15:43
//    添加备注
//
//    通过
//    5772 ms	23.5 MB	Python3	2021/09/27 07:34
//    添加备注
// NOTE: cpp11 is much faster than python3, but with relativity higher memory usage but not that much
}