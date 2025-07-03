#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
/*
    함수 오버로드
    함수의 이름이 같고 인자가 다르면 다른 함수로 작동된다
    이때 리턴은 고려의 대상이 아니다
*/
void myFunction(void){
    cout << "myFunction(void)" << endl;
}
void myFunction(char a){
    cout << "myFunction(char a)" << endl;
}
void myFunction(int a, int b){
    cout << "myFunction(int a, int b)" << endl;
}

int main() {
    SetConsoleOutputCP(65001);
    
    myFunction();
    myFunction('a');
    myFunction(3,5);
    return 0;
}