//
// Created by Tengjun Gao on 10/4/21.
//
#include <iostream>
#include <string>

int main(){
    std::string name;
    std::cout << "Hello what's your name? ";
    std::cin >> name; // to scan only 1 character without whitespace
    std::cout << "Your name is " << name << std::endl;
    std::cout << "\nWhat's your full name?" << std::endl;
    // if only use one getline, it will take last input, and tells me he finds nothing
    std::getline(std::cin, name);
    std::getline(std::cin, name);

    std::cout<< "Hello " << name << ", nice to meet you.\n";
};
