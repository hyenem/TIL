#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
void func3(){
    cout << "func3 before" << endl;
    throw -1;
    cout << "func3 after" << endl;
}
void func2(){
   
        cout << "func2 before" << endl;
        func3();
        cout << "func2 after" << endl;
    
}
void func1(){
  
        cout << "func1 before" << endl;
        func2();
        cout << "func1 after" << endl;
    
}

int main() {
    SetConsoleOutputCP(65001);
    
    try{
        cout << "main before" << endl;
        func1();
        cout << "main after" << endl;
    }catch(int ex){
        cout << "main Exception" << endl;
    }
    return 0;
}