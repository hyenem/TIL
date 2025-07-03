#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

int main() {
    SetConsoleOutputCP(65001);

    int a = 10;
    int b = a;

    printf("%u %u\n", &a, &b);

    int& c = a;
    cout << c << endl;
    printf("%u %u\n", &a, &c);

    int arr[3] = {1, 3, 5};
    int& r1 = arr[0];
    int& r2 = arr[1];
    int& r3 = arr[2];
    
    return 0;
}