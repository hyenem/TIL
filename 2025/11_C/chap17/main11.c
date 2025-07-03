#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
/*
    공용체
*/
union student{
    char c;
    int num;
    double grade;
};

int main() {
    SetConsoleOutputCP(65001);
    
    printf("sizeof = %d\n", sizeof(union student));
    union student s;

    s.c = 'a';
    printf("%c\n", s.c);

    s.num = 10;
    printf("%d\n", s.num);

    s.grade = 10.8;
    printf("%f\n", s.grade);

    printf("%c\n", s.c);
    printf("%d\n", s.num);
    return 0;
}