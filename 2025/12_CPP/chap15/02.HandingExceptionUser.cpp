#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
 
int main() {
    SetConsoleOutputCP(65001);
    int n1, n2;
    cout << " 두 수를 입력하세요 : ";
    cin >> n1 >> n2;
    
    if(n2 == 0){
        cout << "제수의 값이 0 될 수 없습니다 다시 실행하세요" << endl;
    }else {
        cout << "몫 : " << n1/n2 << endl;
        cout << "나머지 : " << n1%n2 << endl;
    }
    
    return 0;
}