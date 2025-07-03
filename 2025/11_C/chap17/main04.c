#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

struct person{
    char* name;
    int age;
};
// 구조체의 동적 메모리 할당
int main() {
    SetConsoleOutputCP(65001);

    struct person p0;

    //동적 선언 방식
    struct person* p = (struct person *)malloc(sizeof(struct person));
    // (*p).name = (char*)malloc(10+1);
    p->name = (char*)malloc(10+1);  //위와 같음

    free(p->name);
    free(p);
    return 0;
}