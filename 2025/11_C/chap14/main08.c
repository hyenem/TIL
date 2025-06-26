#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <string.h>
/*
    배열포인터
    * 1차원 포인터
*/
// void print(int** arr){
//     printf("%d %d\n", **arr, sizeof(arr));
// }

void print(int(*arr)[3]){
    printf("%d %d\n", arr[1][1], sizeof(arr));
}
int main() {
    SetConsoleOutputCP(65001);

    int arr[2][3] = {{1, 3, 5}, {2, 4, 6}};

    int* p = (int*)arr;
    printf("%d\n", *(p+5));

    // print(arr);
    int (*ap)[3] = arr;
    printf("%d %d \n", ap[0][0], ap[1][2]);

    print(arr);

    return 0;
}