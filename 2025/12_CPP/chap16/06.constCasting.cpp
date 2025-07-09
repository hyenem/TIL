#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

void print(int& a){
    a++;
}

int main() {
    SetConsoleOutputCP(65001);

    const int a = 10;
    const int& b = a;

    int& c = const_cast<int&>(a);
    c++;

    // print(a);
    print(const_cast<int&>(a));

    return 0;
}