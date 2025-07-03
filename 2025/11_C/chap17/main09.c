#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

typedef struct person{
    char name[10+1];
    int age;
} Person;

// 자기참조 구조체
typedef struct personNode{
    int num;
    struct personNode* next;
    Person* p;
} PersonNode;

int main() {
    SetConsoleOutputCP(65001);
    
    PersonNode a = {1};
    PersonNode b = {2};
    PersonNode c = {3};
    
    a.p = (Person*)malloc(sizeof(Person));
    strcpy(a.p->name, "둘리");
    a.p->age = 7;

    b.p = (Person*)malloc(sizeof(Person));
    strcpy(b.p->name, "도우너");
    b.p->age = 8;

    c.p = (Person*)malloc(sizeof(Person));
    strcpy(c.p->name, "또치");
    c.p->age = 9;

    a.next = &b;
    b.next = &c;
    c.next = NULL;

    PersonNode* cur = &a;
    while(cur!=NULL){
        printf("%d %s %d\n", cur->num, cur->p->name, cur->p->age);
        cur = cur->next;
    }

    free(a.p);
    free(b.p);
    free(c.p);
    return 0;
}