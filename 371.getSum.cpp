/*
 *
Code
Testcase
Test Result
Test Result
371. Sum of Two Integers
Medium
Topics
Companies
Given two integers a and b, return the sum of the two integers without using the
operators + and -.



Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5


Constraints:

-1000 <= a, b <= 1000
Accepted
504.2K
Submissions
963.9K
Acceptance Rate
52.3%
Topics
Companies
Similar Questions
Discussion (74)

Choose a type



Copyright ©️ 2024 LeetCode All rights reserved*/

#include <iostream>

class Solution {
public:
  int getSum(int a, int b) {
    return b == 0 ? a : getSum(a ^ b, (unsigned int)(a & b) << 1);
  }
};

int main() {
  Solution S1;
  std::cout << S1.getSum(1, 2) << std::endl; // 3
  std::cout << S1.getSum(2, 3) << std::endl; // 5
  return 0;
}
