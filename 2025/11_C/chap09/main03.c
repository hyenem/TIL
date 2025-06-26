#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

void change(int a, int b){
    int tmp = a;
    a = b;
    b = tmp;
}

void change2(int* a, int* b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

// int change3(const int a, const int b){
int* change3(int* a, int* b){
    (*a)++, (*b)--;
    static int res;
    res = *a + *b;
    return &res;
}

int main() {
    SetConsoleOutputCP(65001);
    
    int a = 5; int b = 10;
    // const int a = 1;
    // const int b = 5;

    change(a, b);
    printf("main %d %d \n", a, b);

    change2(&a, &b);
    printf("main %d %d \n",a, b);

    int* res = change3(&a, &b);
    printf("main res= %d \n", *res);
    
    return 0;
}