#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int print(int arr[3]){
    printf("%d \n", sizeof(arr));
    for (size_t i = 0; i < 3; i++)
    {
        printf("%d ", arr[i]);
    }
}

int main() {
    SetConsoleOutputCP(65001);
    
    int arr[3] = {1, 3, 5};
    int arr2[3] = {11, 33, 55};
    printf("%d %d \n", arr[1], *(arr+1));
    // 변수의 주소를 바꿀수는 없다
    // arr = arr+1;

    int* pa = arr;
    printf("%d %d %d \n", *(pa+0), *(pa+1), pa[2]);

    pa = arr2;
    printf("%d %d %d \n", *(pa+0), *(pa+1), pa[2]);

    printf("%u \n", &pa);

    printf("%d \n", sizeof(arr));
    print(arr);

    return 0;
}