#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
/*
    배열의 동적 메모리 할당
*/

int main() {
    SetConsoleOutputCP(65001);
    
    //정적 선언 방식
    int arr[3];

    //동적 선언 방식
    int *p = (int*)malloc(sizeof(int)*3);
    memset(p, 0, sizeof(int)*3); //초기화
    if(p==NULL){
        printf("메모리 할당 실패");
        return -1;
    }
    *p = 1;
    *(p+1) = 3;
    *(p+2) = 5;

    int i = 0;
    for (size_t i = 0; i < 3; i++)
    {
        printf("%d\n", p[i]);
    }
    

    free(p);
    return 0;
}