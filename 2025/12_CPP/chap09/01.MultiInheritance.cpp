#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
/*
    다중상속의 문제점
        1. 모호성
            해결 : 범위연산자를 이용하여 클래스를 지정해주어야 한다
        2. 마름모 상속구조가 만들어지면 같은 객체가 여러개 만들어진다
            해결 : 
*/
class Grand{
public :
    int num;
};
class Father : virtual public Grand{
public :
    virtual void print(){cout << "father print " << endl;}
};
class Mother : virtual public Grand{
public :
    virtual void print(){cout << "mother print " << endl;}
};
class Son: public Father, public Mother{
public :
    // virtual void print(){cout << "son print "<<endl;}
};

int main() {
    SetConsoleOutputCP(65001);

    Son* s = new Son;
    s->Father::print();

    Father* f = new Son;
    f->print();

    Mother* m = new Son;
    m->print();

    return 0;
}