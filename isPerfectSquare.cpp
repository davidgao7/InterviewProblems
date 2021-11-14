//
// Created by Tengjun Gao on 11/14/21.
//

using namespace std;

#include "iostream"

class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num == 0 or num == 1)return true;
        int l = 0, r = num;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (long(mid) * long(mid) < long(num)) {
                l = mid+1; //一个一个来
            }
            else if (long(mid) * long(mid) > long(num)) {
                r = mid-1;
            }
            else{
                return true;
            }
        }
        return false;
    }
};

int main() {
    Solution *s = new Solution();
    int num = 100;
    printf("is %d perfect square? %d\n", num, s->isPerfectSquare(num));
}