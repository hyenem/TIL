#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

int main() {
    SetConsoleOutputCP(65001);

    cout << true << endl;
    cout << false << endl;

    bool a;
    a = true;
    a = false;

    return 0;
}