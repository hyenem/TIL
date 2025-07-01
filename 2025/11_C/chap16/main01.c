#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
/*
    동적 메모리 할당
*/
int main() {
    SetConsoleOutputCP(65001);
    
    auto int a = 10;
    /*
        메모리 할당과 값 입력
    */

    int *p = (int*)malloc(sizeof(int));
    *p = 10;
    (*p)++;
    free(p);

    return 0;
}