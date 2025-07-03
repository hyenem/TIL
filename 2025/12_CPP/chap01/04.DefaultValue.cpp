#include <iostream>
#include <cstdlib>
#include <windows.h>

using namespace std;

/*
    함수 인자에 기본값을 줄 수 있는데
    이때는 뒤의 인자부터 주어야 한다.
*/

void print(int a = 10, int b = 5){

}
void print2(int a, int b=9){

}

int main() {
    SetConsoleOutputCP(65001);

    print(3, 4);
    print(3);
    print();

    print2(1, 2);

    return 0;
}