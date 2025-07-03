#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

class Person{
private:
    int age;
protected:

public:
    //기본 생성자
    Person(){};
    Person(int age){this->age = age;}
    char name[10];
    void info(){
        cout << name <<", " << age << endl;
    }
};

int main() {
    SetConsoleOutputCP(65001);

    //정적
    Person sp(4);
    sp.info();

    //동적
    Person* pp = new Person(10);
    pp->info();

    //new와 malloc은 동작방식이 다릅니다.
    // malloc은 공간만 잡음.
    //new 는 기본으로 만들어주는 것이 다름.
    delete pp;

    return 0;
}