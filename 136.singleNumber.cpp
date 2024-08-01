/*
 * 136. Single Number
Easy
Topics
Companies
Hint
Given a non-empty array of integers nums, every element appears twice except for
one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1


Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears
only once. Accepted 3M Submissions 4M Acceptance Rate 73.7% Topics Array Bit
Manipulation Companies Hint 1 Think about the XOR (^) operator's property.
Similar Questions
Single Number II
Medium
Single Number III
Medium
Missing Number
Easy
Find the Duplicate Number
Medium
Find the Difference
Easy
Find the XOR of Numbers Which Appear Twice
Easy
*/

#include <vector>
using namespace std;

class Solution {
public:
  int singleNumber(vector<int> &nums) {
    // XOR all the elements in the array (XOR of two same numbers is 0)
    // different will get 1
    int result = 0; // n XOR 0 = n
    for (int i = 0; i < nums.size(); i++) {
      result ^= nums[i];
    }
    return result;
  }
};
