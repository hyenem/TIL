#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

void change(int a, int b){
    int tp = a;
    a = b;
    b = tp;
    printf("change %d %d\n",a,b);
}

void change2(int* a, int* b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int* change3(int* a,int* b){
    *a++, *b--;
    int res = *a + *b;
    return &res;
}

int main() {
    SetConsoleOutputCP(65001);
    
    int a = 10;
    int b = 5;
    change(a,b);
    printf("main %d %d\n",a,b);

    change2(&a,&b);
    printf("main %d %d \n",a,b);

    int* res = change3(&a, &b);
    printf("main  res = %d \n",*res);
    return 0;
}
