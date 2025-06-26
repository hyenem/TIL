#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
 
int main() {
    SetConsoleOutputCP(65001);
    int arr[3];
    memset(arr,0,sizeof(arr));

    arr[3] = 10;

    printf("%d \n",arr[3]);
    return 0;
}