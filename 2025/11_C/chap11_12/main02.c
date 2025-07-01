#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
 
int main() {
    SetConsoleOutputCP(65001);
 
    char a;
    int b;
    a = getchar();
    putchar(a);

    // scanf("%c %d",&a, &b);
    // printf("%c %d",a,b);


    
    return 0;
}