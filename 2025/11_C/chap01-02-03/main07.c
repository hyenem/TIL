#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
 
int main() {
    SetConsoleOutputCP(65001);
    
    int a = 10, b = 5;
    int rs = a + b;
    printf("a = %d &a = %u , %d\n",a,&a,*&a);
    return 0;
}