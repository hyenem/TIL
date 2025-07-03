#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
/*
    inline 함수를 선언하면 컴파일 시 변환이 되어집니다.
    단 코드가 길어지거나 변환이 어려워지면 변환하지 않습니다.
*/
inline int add(int a, int b){
    return a+b;
}

int main() {
    SetConsoleOutputCP(65001);

    cout << add(4, 7) << endl;

    return 0;
}