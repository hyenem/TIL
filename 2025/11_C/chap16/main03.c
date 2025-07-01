#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
/*
    동적 메모리 재할당
*/
int main() {
    SetConsoleOutputCP(65001);

    //calloc
    // 메모리를 동적할당하고 0으로 초기화까지 한다
    // calloc(개수, 요소값 크기)
    int* p = (int*)calloc(3, sizeof(int));
    if(p==NULL){
        printf("메모리 할당 실패");
        return -1;
    }
    p[0] = 1;
    p[1] = 3;
    *(p+2) = 5;
    printf("%d\n", *(p+2));

    printf("before p = %u\n", p);
    // realloc
    // 할당된 메모리의 크기를 변경합니다.
    // memcpy 함수가 내부적으로 실행되어 기존의 값이 복사됩니다.
    // 주소 바뀌면  free도 realloc이 해줌
    p = realloc(p, sizeof(int)*500);
    printf("after p = %u\n", p);
    printf("%d\n", *(p+2));

    free(p);
    return 0;
}