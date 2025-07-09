#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
/*
    Function Template
        함수를 만드는 틀
*/
int add(int a, int b){
    cout << "일반함수 add T = "  ;
    return a+b;
}
template <typename T> 
T add(T a, T b){
    cout << "템플릿함수 add T = " ;
    return a+b;
}
template <typename T, class F> 
F add(T a, F b){
    cout << "템플릿함수 add T F = " ;
    return a+b;
}


int main() {
    SetConsoleOutputCP(65001);
    int a = 10, b = 5;
    // 일반함수
    cout << add(a,b) << endl;

    // 템플릿함수
    cout << add<int>(3,4) <<endl;
    cout << add<double>(3.1,4.2) <<endl;

    cout << add<int, double>(3,3.14) << endl;
    return 0;
}