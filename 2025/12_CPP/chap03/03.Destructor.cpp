#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
class Person{
private :
    int num = 0;
    char* name;
public :
    Person(){}
    // Person(int num){this->num = num;}
    Person(int num, char* name):num(num){
        //깊은 복사
        name = (char*)malloc(strlen(name));
        strcpy(this->name, name);
    }
    void print(){
        cout << num << endl;
    }
};
int main() {
    SetConsoleOutputCP(65001);

    Person p(10, "둘리");
    p.print();

    return 0;
}