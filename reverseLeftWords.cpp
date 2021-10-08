//
// Created by Tengjun Gao on 10/8/21.
//
#include "string"
using namespace std; // for cout, endl, string class

class Solution {
public:
    string reverseLeftWords(string s, int n) {
        string answer = "";
        for(int i = n; i < s.length(); i++){
            answer+=s[i];
        }
        for (int i = 0; i < n; i++) {
            answer+=s[i];
        }
        return answer;
    }
};

int main(){
    Solution *solution = new Solution();
    string s = "abcdefg";
    printf("origin: %s\n", s.c_str());
    int k = 2;
    string answer = solution->reverseLeftWords(s, k);
    const char* string1 = answer.c_str();
    printf("%s", string1); // NOTE: stdio.h, %s need to be char* not string
    // The pointer is such that the range [c_str(); c_str() + size()] is valid and the values
    // in it correspond to the values stored in the string with an additional null character
    // after the last position.
}