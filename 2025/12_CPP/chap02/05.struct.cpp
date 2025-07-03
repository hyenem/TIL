#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

typedef struct{
    char name[20];
    int age;

    //cpp에서는 구조체 안에 함수를 선언할 수 있습니다.
    void print(){
        // 구조체가 생성될 떄 this가 자동으로 만들어지고
        // this에는 생성된 구조체의 주소가 저장됨
        cout << this->name << ", " << age << endl;
    }
} Person;

int main() {
    SetConsoleOutputCP(65001);
    
    // 정적 선언
    Person p = {"홍길동", 9};
    p.print();

    //동적 선언
    Person* sp = new Person;
    sp -> age = 9;
    strcpy(sp->name, "둘리");
    sp->print();
    delete sp;

    return 0;
}