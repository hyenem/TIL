#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

typedef int INT64;
typedef unsigned int UINT;

// 구조체의 타입 재정의
typedef struct person{
    char name[10];
    int age;
} Person;

int main() {
    SetConsoleOutputCP(65001);
    
    INT64 a;
    a=10;

    UINT b = 500;

    struct person p;
    Person p1;
    p1.age = 10;

    Person* p2;
    p2->age = 30;

    return 0;
}