#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
class Person{
private :
    int num = 0;
    char* name;
    static int sa;
public :
    Person(){}
    // Person(int num){this->num = num;}
    Person(int num, const char* name):num(num){
        //깊은 복사
        // this->name = (char*)malloc(strlen(name));
        this->name = new char[strlen(name)+1];
        strcpy(this->name, name);
    }
    //소멸자
    ~Person(){
        delete[] name;
        cout<<"destructor"<<endl;
    }
    void print(){
        cout << num << endl;
    }
};
int Person::sa = 20;
// static 변수 초기화

int main() {
    SetConsoleOutputCP(65001);

    Person p(10, "둘리");
    p.print();

    return 0;
}