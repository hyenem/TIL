#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

int main() {
    SetConsoleOutputCP(65001);

    int a = 1233;
    char* p = reinterpret_cast<char*>(&a);

    return 0;
}