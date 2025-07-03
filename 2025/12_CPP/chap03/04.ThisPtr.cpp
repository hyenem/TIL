#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
/*
    this 포인터 변수
        멤버 함수 안에서 자동으로 생성되는 변수
*/

class Person{
private :
    int num1, num2;
public :
    Person(){}
    Person(int n1, int n2): num1(n1), num2(n2){};
    void print(){
        cout << "num : " << this->num1 << ", " << this->num2 << endl;
    }
    Person* getNum1(){
        cout << num1 << endl;
        return this;
    }
    Person* getNum2(){
        cout << num2 << endl;
        return this;
    }
    Person& getNumval(){
        return *this;
    }
};

int main() {
    SetConsoleOutputCP(65001);

    Person p(1, 2);
    p.print();

    p.getNum1()->getNum2()->getNum1()->getNum2();
    p.getNumval().getNumval().getNumval().getNumval();

    return 0;
}