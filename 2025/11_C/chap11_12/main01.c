#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
 
int main() {
    SetConsoleOutputCP(65001);
 
    for (size_t i = 0; i < 255; i++)
    {
        printf("%d = %c\n",i,i);
    }
    

    return 0;
}