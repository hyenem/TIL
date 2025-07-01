#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
/*
    포인터변수
*/ 
int main() {
    SetConsoleOutputCP(65001);
    
    char c = 'A';
    char* pc = &c;

    printf("%c %u %u %c \n",c,&c,pc, *pc);

    c = 'B';
    
    printf("%c  \n",*pc);

    *pc = 'C';
    printf("%c  \n",c);

    int a = 10, b = 5, res = 0;
    int* pa = &a;
    int* pb = &b;
    res = *pa + *pb;
    printf("%d  \n",res);

    printf("%d %d %d %d\n",sizeof(c),sizeof(pc),sizeof(a),sizeof(pa));
    return 0;
}