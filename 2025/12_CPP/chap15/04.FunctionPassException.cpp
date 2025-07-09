#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

int divide(int a, int b){
    
    if(b==0) throw b;
    // 예외가 발생할수 있는코드
    cout << "몫 : " << a/b << endl;
    cout << "나머지 : " << a%b << endl;
    
}
int main() {
    SetConsoleOutputCP(65001);
    int n1, n2;
    cout << " 두 수를 입력하세요 : ";
    cin >> n1 >> n2;
    
    try{
        divide(n1,n2);
        cout << "몫과 나머지가 출력되었습니다" << endl;
    }catch(int ex){
        cout << "나누셈의 제수는 "<< ex << " 될 수 없습니다" << endl;
    }
    
    
    return 0;
}