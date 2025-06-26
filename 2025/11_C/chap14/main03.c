#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <string.h>

int main() {
    SetConsoleOutputCP(65001);
    
    int arr1[3] = {1, 3, 5};
    int arr2[5] = {2, 4, 6, 8, 0};

    int* p1 = arr1;
    int* p2 = arr2;

    int* parr[2] = {p1, p2};

    printf("%d %d \n", parr[0][0], parr[1][3]);

    return 0;
}