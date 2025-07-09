#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

int main() {
    SetConsoleOutputCP(65001);

    int n1, n2;
    cout << "두 수를 입력하세요 : " << endl;
    cin >> n1 >> n2;

    try{
        if(n2==0) throw n2;
        // 예외가 발생할 수 있는 코드
        cout << "몫 : " << n1/n2 << endl;
        cout << "나머지 : " << n1%n2 << endl;
    } catch(int ex) {
        cout << "제수는 " << ex <<"이 될 수 없습니다. 다시 실행하세요." << endl;
    }

    return 0;
}