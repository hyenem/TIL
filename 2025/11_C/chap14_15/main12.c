#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

/*
    void 포인터 변수
     모든 변수의 주소를 저장할 수 있으나
     사용할 때는 꼭 형변환해서 사용하여야 한다.
*/
int main() {
    SetConsoleOutputCP(65001);
    
    int a = 10;
    char c = 'a';

    void* p;

    p = &a;
    printf("a = %d \n", *(int*)p);

    p = &c;
    printf("c = %c \n", *(char*)p);

    return 0;
}