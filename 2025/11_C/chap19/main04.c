#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#define NAME_CAT(x, y) (x ## y)
#define PRINT_EX(x) printf(#x "= %d\n", x)
#define PRINT_STRING(x) printf(#x)


int main() {
    SetConsoleOutputCP(65001);
    
    int a1, a2;

    NAME_CAT(a, 1) = 10;
    NAME_CAT(a, 2) = 5;

    PRINT_EX(a1 + a2);
    PRINT_EX(a1 - a2);

    PRINT_STRING(THIS IS STRING\n);
    
    return 0;
}