#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

template <class T>
void print(){
    static int num = 1;
    cout << num++ << endl;
}
int main() {
    SetConsoleOutputCP(65001);

    print<int>();
    print<int>();
    print<int>();

    print<double>();
    print<double>();
    print<double>();
    
    return 0;
}