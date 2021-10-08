//
// Created by Tengjun Gao on 10/8/21.
//
#include "string"
#include "iostream"

using namespace std;

class Solution {
public:
    string replaceSpace(string s) {
        string answer = "";
        for(char c: s){
            if(c == ' '){
                answer.append("%20");
            }else{
                answer+=c;
            }
        }
        return answer;
    }
};

int main(){
    string s = "We are happy.";
    Solution *solution = new Solution();
    string answer = solution->replaceSpace(s);
    cout<< answer << "\n";
};