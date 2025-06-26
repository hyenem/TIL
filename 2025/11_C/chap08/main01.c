#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
/*
    배열
     정의 : 같은데이타의 순서적 나열 (c 언어에서의 배열을 연속된 메모리상에서의 순서를 의미합니다)
     특정 : 선언과 동시에 크기가 결정되어야 하고 크기변경이 불가하다
     선언방식 : 정적선언방식과 동적선언방식이 있다     
*/ 
int main() {
    SetConsoleOutputCP(65001);
    
    int arr[3];
    int i=0;
    arr[0] = 1;
    arr[1] = 3;
    arr[2] = 5;
    
    printf("arr size = %d \n",sizeof(arr)/sizeof(int));

    for(i=0;i<3;i++){
        printf("arr[%d] = %d \n",i,arr[i]);
    }
    
    printf("arr 의 이름은 ? %x \n",arr);
    
    printf(" *arr 의 이름은 ? %d \n", *(arr+0), arr[0]);
    return 0;
}