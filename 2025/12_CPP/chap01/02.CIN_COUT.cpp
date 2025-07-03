#include <iostream>
#include <windows.h>
using namespace std;

int main() {
    SetConsoleOutputCP(65001);

    cout << "두 정수를 입력하세요 "<< std::endl;
    int a, b;
    cin >> a >> b;

    cout << a <<","<< b<< std::endl;
    
    std::cout << "문자열을 입력하세요 "<< std::endl;
    char name[20+1];
    std::cin >> name;
    std::cout << "입력받은 문자열은 "<< name << std::endl;

    return 0;
}