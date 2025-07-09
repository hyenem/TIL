#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

void func3(){
    throw -1;
}
void func2(){
    try{
        cout << "func3 before" << endl;
        func3();
        cout << "func3 after" << endl;
    } catch(int ex){
        cout << "func2 Exception" << endl;
    }
}
void func1(){
    try{
        cout << "func2 before" << endl;
        func2();
        cout << "func2 after" << endl;
    } catch(int ex){
        cout << "func1 Exception" << endl;
    }
}
int main() {
    SetConsoleOutputCP(65001);

    try{
        cout << "func1 before" << endl;
        func1();
        cout << "func1 after" << endl;
    } catch(int ex){
        cout << "main Exception" << endl;
    }

    return 0;
}