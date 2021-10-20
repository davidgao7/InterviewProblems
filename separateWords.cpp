//
// Created by Tengjun Gao on 10/19/21.
//
#include "vector"
#include "string"
#include "iostream"
#include "sstream"

using namespace std;

int main() {

    vector<string> words;
    stringstream ss;
    ss << "some random words";
    string word;

    while (getline(ss, word, ' ')) {
        words.push_back(word);
    }

    cout << "using regular for loop" << endl;
    for (int i = 0; i < words.size(); i++) {
        cout << words[i] << endl;
    }

    cout << "using auto for loop" << endl;
    for (auto x: words) cout << x << endl;

    // copy string
    string s1 = "hello";
    string s2(s1, 2);
    string s3 = s1 + "  not hello";
    string s4;
    s4 = s3;
    s4.erase(7, s4.length() - 1); // 从第7个地方开始erase（包括第七个地方）
    cout<<s1<<endl; // hello
    cout<<s2<<endl; // llo
    cout<<s3<<endl; // hello not hello
    cout<<s4<<endl; //
    return 0;
}