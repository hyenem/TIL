#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
/*
    이중포인터
*/ 
int main() {
    SetConsoleOutputCP(65001);
 
    int a = 10;
    int* pa = &a;
    int** ppa = &pa;

    printf("%u %u %u\n",ppa, *ppa, **ppa);
    **ppa = 20;
    printf("%u\n",a);
    return 0;
}