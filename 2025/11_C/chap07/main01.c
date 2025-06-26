#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include "myfunction.h"



int main() {
    SetConsoleOutputCP(65001);
    int a = 10, b = 5, res = 0;

    res = add(a, b);
    // res = minus(a, b);
    // res = cross(a, b);
    // res = division(a, b);

    printf("res = %d \n", res);
    return 0;
}

