/*
Given two non-negative integers num1 and num2 represented as strings, return the
product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to
integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
*/

using namespace std;
#include <string>;

class Solution {
public:
  string multiply(string num1, string num2) {

    // anything multiplied by 0 is 0
    if ('0' == num1[0] || '0' == num2[0]) {
      return "0";
    }

    // make a list of zeros of size num1.size() + num2.size()
    string result(num1.size() + num2.size(), '0');

    // reverse both num1 and num2
    // NOTE: this is how to reverse a string in c++
    num1 = string(num1.rbegin(), num1.rend());
    num2 = string(num2.rbegin(), num2.rend());

    // multiply each digit of num1 with each digit of num2
    // and add the result to the result string
    for (int i = 0; i < num1.size(); i++) {
      for (int j = 0; j < num2.size(); j++) {
        int digit = (num1[i] - '0') * (num2[j] - '0') + (result[i + j] - '0');
        result[i + j] = digit % 10 + '0';
        result[i + j + 1] += digit / 10;
      }
    }

    // get rid of leading zeros
    // 1. reverse the result string
    result = string(result.rbegin(), result.rend());
    int begin = 0;
    while (begin < result.size() && result[begin] == '0') {
      begin++;
    }

    // 2. return the result string
    return result.substr(begin);
  }
};
