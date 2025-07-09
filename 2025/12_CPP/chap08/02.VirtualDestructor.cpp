#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
class Father{
public :
    int num = 10;
    Father(){cout << "Father 생성자" << endl;}
    Father(const Father& f){cout << "Father 복사생성자" << endl;}
    virtual ~Father(){cout << "Father 소멸자" << endl;}
    virtual void print(){cout << "father print num = "<<num<<endl;}
};
class Son : public Father{
public :
    int x = 1110;
    Son(){cout <<"Son 생성자"<< endl;}
    virtual ~Son(){cout << "Son 소멸자" << endl;}
    virtual void print(){cout << "son print num = "<<num<<endl;}
};

int main() {
    SetConsoleOutputCP(65001);

    Father* f = new Father();
    cout << sizeof(*f) << endl;
    delete f;

    Son* s = new Son();
    cout << sizeof(*s) << endl;
    delete s;

    Father* fs = new Son();
    delete fs;

    return 0;
}