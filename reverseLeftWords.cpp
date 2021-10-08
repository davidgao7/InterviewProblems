//
// Created by Tengjun Gao on 10/8/21.
//
#include "string"
using namespace std; // for cout, endl, string class

class Solution {
public:
    string reverseLeftWords(string s, int n) {
        return s;
    }
};

int main(){
    Solution *solution = new Solution();
    string s = "abcdefg";
    int k = 2;
    string answer = solution->reverseLeftWords(s, k);
    const char* string1 = answer.c_str();
    printf("%s", string1); // stdio.h, %s need to be char* not string
    // The pointer is such that the range [c_str(); c_str() + size()] is valid and the values
    // in it correspond to the values stored in the string with an additional null character
    // after the last position.
}