#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

int print(int* );

int main() {
    SetConsoleOutputCP(65001);
    // 포인트변수를 이용하여 배열을 처리할수 있다
    
    int arr[5] = {1,3,5};
    int arr2[3] = {11,33,55};
    printf("%d %d\n",arr[1] , *(arr+1));
    // 변수의 주소를 바꿀수는 없다
    //arr = arr+1;
    
    int* pa = arr;
    printf("%d %d %d\n", *(pa+0) , *(pa+1), pa[2]);

    pa = arr;
    printf("%d %d %d\n", *(pa+0) , *(pa+1), pa[2]);

    printf("%u \n", &pa);
    
    //arr =  arr2;
    printf("%d\n",sizeof(arr));
    
    print(arr);
    // 배열의 주소를 바꿀수는 없다
    //arr++;
    // 포인트변수의 값을 변경할수는 있다
    pa++;
    return 0;
}

int print(int* arr){
    printf("%d\n",sizeof(arr));
    for (size_t i = 0; i < 3; i++)
    {
       printf("%d ",arr[i]);
    }
}