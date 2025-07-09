#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

class Person{
private :
    int num;
public :
    Person(){}
    Person(int num):num(num){}
    ~Person(){}
    void print(){cout << "print = " << num << endl;}
    void print()const{cout << "const print = " << num << endl;}
};
int main() {
    SetConsoleOutputCP(65001);

    Person p(100);
    p.print();

    // 객체 생성을 const로 하게 되면
    // const 멤버 변수나 const 멤버 함수만 호출이 가능
    const Person sp(100);
    sp.print();

    return 0;
}