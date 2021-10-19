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
    ss<<"some random words";
    string word;

    while (getline(ss, word, ' ')) {
        words.push_back(word);
    }

    cout<<"using regular for loop"<<endl;
    for (int i = 0; i < words.size(); i++){
        cout << words[i] << endl;
    }

    cout<<"using auto for loop"<<endl;
    for (auto x: words) cout << x << endl;

    return 0;
}