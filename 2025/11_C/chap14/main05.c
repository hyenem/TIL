#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <string.h>
/*
    이중 포인터
*/
int main() {
    SetConsoleOutputCP(65001);

    int a = 10;
    int* pa = &a;
    int** ppa = &pa;
    printf("%u %u %u \n", ppa, *ppa, **ppa);

    return 0;
}