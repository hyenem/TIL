#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

// 구조체의 타입재정의
typedef struct person{
    char name[10];
    int age
} Person;

//구조체의 포인트 배열 심화
int main() {
    SetConsoleOutputCP(65001);
    
    Person* ps[3];
    for (size_t i = 0; i < 3; i++)
    {
        ps[i] = (Person*)malloc(sizeof(Person));
    }
    strcpy(ps[0]->name, "둘리");
    ps[0]->age = 8;
    strcpy(ps[0]->name, "도우너");
    ps[1]->age = 9;
    strcpy(ps[0]->name, "또치");
    ps[2]->age = 10;

    Person** pp = ps;
    for (size_t i = 0; i < 3; i++)
    {
        printf("%s %d\n", pp[i]->name, pp[i]->age);
        printf("%s %d\n", (*(pp+i))->name, (*(pp+i))->age);
        printf("%s %d\n", (*(*(pp+i))).name, (*(*(pp+i))).age);
    }
    

    for (size_t i = 0; i < 3; i++)
    {
        free(ps[i]);
    }
    
    return 0;
}