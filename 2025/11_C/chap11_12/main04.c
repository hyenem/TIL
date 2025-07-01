#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
 
int main() {
    SetConsoleOutputCP(65001);
    char str[20+1];
    char* p = gets(str);

    puts(str);

    return 0;
}