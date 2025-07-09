#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
class Father{
public :
    int num = 10;
    Father(){cout << "Father 생성자" << endl;}
    Father(const Father& f){cout << "Father 복사생성자" << endl;}
    ~Father(){cout << "Father 소멸자" << endl;}
    void print(){cout << "father print num = "<<num<<endl;}
};
class Son : public Father{
public :
    Son(){cout <<"Son 생성자"<< endl;}
    ~Son(){cout << "Son 소멸자" << endl;}
    virtual void print(){cout << "son print num = "<<num<<endl;}
};

int main() {
    SetConsoleOutputCP(65001);

    // Son s;
    // Father f = s;

    Father* fp = new Father();
    fp->print();

    Son* sp = new Son();
    sp->print(); 

    Father* fsp = new Son();
    // Son* ss = (Son*)sp;
    // java 는 동적 바인딩
    // C++ 는 정적 바인딩
    fsp->print();       //fater호출

    return 0;
}