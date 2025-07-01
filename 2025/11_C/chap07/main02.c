#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

void change(int a, int b){
    int tmp = a;
    a = b;
    b = tmp;
    printf("change a = %d, b = %d\n",a,b);
}

int main() {
    SetConsoleOutputCP(65001);
    int a = 10, b= 5;

    change(a,b);

    printf("main a = %d, b = %d\n",a,b);
    
    return 0;
}