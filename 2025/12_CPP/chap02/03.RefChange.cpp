#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
/*
    참조형은 변수에 이름을 하나 더 붙이는 것.
    함수의 파라미터 타입이 참조형이면 주소변수와 같은 효과를 냅니다.
    함수의 리턴타입이 참조형이면 호출한 쪽의 변수는 참조형 일반형 다 가능ㅎ다ㅏ
    하지만 두개의 의미는 다르다.
    일반형이면 복사가 이루어지고
    참조형이면 이름 하나 더 붙이는 것.
*/
void change(int* a, int b){
    (*a)++;
}
void change2(int& a, int& b){
    int tmp = a;
    a = b;
    b = tmp;
}
int& change3(int a){
    static int b = a;
    b++;
    printf("%u \n", &b);
    return b;
}
int main() {
    SetConsoleOutputCP(65001);

    int a = 10, b = 5;
    change(&a, b);
    cout << "main a = "<< a << endl;
    change2(a, b);
    cout << "main a = "<< a << ", b= "<< b << endl;

    a = 10;
    int& res = change3(a);
    cout << "res = "<< res << endl;
    printf("%u \n", &res);

    return 0;
}