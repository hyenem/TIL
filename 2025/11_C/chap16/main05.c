#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
/*
    main함수의 초기값
*/
//main05.exe hong park
int main(int argc, char** argv) {
    SetConsoleOutputCP(65001);
    
    printf("%d\n", argc);
    for (size_t i = 0; i < argc; i++)
    {
        printf("%s\n", argv[i]);
    }
    
    return 0;
}