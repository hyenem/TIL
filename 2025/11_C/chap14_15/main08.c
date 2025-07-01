#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
/*
    배열포인터
     특성 : 1차원포인터

*/
void print(int (* app)[3]);
int main() {
    SetConsoleOutputCP(65001);
 
    int arr[2][3] = {{1,3,5},{2,4,6}};
    int*p = (int*)arr;
    printf("%d\n", *(p+5));

    // 배열포인터
    int (*ap)[3] = arr;
    printf("%d %d\n",ap[0][0],ap[1][2]);
    print(arr);
    return 0;
}
void print(int (*arr)[3]){
    printf("%d sizeof() = %d \n", arr[1][1], sizeof(arr));
}