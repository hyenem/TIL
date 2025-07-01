#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
// #pragma pack(1) //구조체에 정확하게 1바이트씩만 잘라서 넣음
/*
    user define datatype
    구조체
*/

struct person{
    char name[20+1];
    int age;
    long i;
};

void print(struct person p){
    p.age++;
    printf("print %s %d\n", p.name, p.age);
}

int main() {
    SetConsoleOutputCP(65001);
    
    //구조체 변수는 데이터 변수다
    struct person p = {"둘리", 7, 100};
    p.age++;
    strcpy(p.name, "고길동");
    printf("%s %d\n", p.name, p.age);

    print(p);
    printf("main %s %d\n", p.name, p.age);

    printf("sizeof p = %d\n", sizeof(p));

    //구조체의 복사
    struct person p2 = p;
    printf("main %s %d\n", p2.name, p2.age);
    
    return 0;
}