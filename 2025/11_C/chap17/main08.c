#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
// 구조체 안에 구조체
typedef struct person{
    char name[10+1];
    int age;
} Person;

typedef struct student{
    int num;
    Person p;
} Student;
typedef struct student2{
    int num;
    Person* p;
} Student2;

int main() {
    SetConsoleOutputCP(65001);
    
    //정적 선언 방식
    Student s;
    s.num = 1;
    strcpy(s.p.name, "둘리");
    s.p.age = 7;

    //동적 선언 방식
    Student2* s2 = (Student2*)malloc(sizeof(Student2));
    s2 -> p = (Person*)malloc(sizeof(Person));
    s2->p->age = 10;
    strcpy(s2->p->name, "또치");
    s2->num = 2;

    free(s2->p);
    free(s2);
    return 0;
}