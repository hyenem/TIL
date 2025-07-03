#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
/*
    const 키워드에 대한 정리
*/

class Person{
private :
    int age = 10;
public:
    // 함수 뒤에 const가 붙으면 안에서 맴버변수를 바꿀 수 없음
    void changeAge(int add) const{
        // age = age + add;
        // const 함수 안에서는 const 함수만 호출 가능
        change();
        cout << age << endl;
    }
    void change() const{
        cout << "change" << endl;
    }
};
//전역함수
void change(char name[]){
    cout << "name[] " << name << endl;
}
void change(const char* name){
    cout << "const char* " << name << endl;
}
int main() {
    SetConsoleOutputCP(65001);
    
    char name[] = "둘리";
    change(name);
    change("도우너");

    // 변수를 상수화
    const int a = 10;
    //a = 20; 에러
    
    // const 키워드를 포인트변수 앞에 붙임으로써 값 변경을 할 수 없게 한다.
    const int* p = &a;
    // (*p)++;
    cout << *p << endl;

    // const 키워드가 포인트 타입 뒤에 붙으면 포인트 변수의 값 변경이 불가하다.
    int b = 20, c = 30;;    
    int* const p2 = &b;
    // p2 = &c;

    Person sp;
    sp.changeAge(10);

    return 0;
}