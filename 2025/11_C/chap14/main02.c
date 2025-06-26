#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <string.h>

int main() {
    SetConsoleOutputCP(65001);
    puts("3명의 이름을 입력하세요.");
    char name[3][20+1];

    for (size_t i = 0; i < 3; i++)
    {
        gets(name[i]);
        puts(name[i]);
    }
    
    
    return 0;
}