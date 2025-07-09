#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

int main() {
    SetConsoleOutputCP(65001);

    int n1, n2;
    cout << "두 수를 입력하세요 : " << endl;
    cin >> n1 >> n2;

    cout << "몫 : " << n1/n2 << endl;
    cout << "나머지 : " << n1%n2 << endl;


    return 0;
}