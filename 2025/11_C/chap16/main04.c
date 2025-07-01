#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
/*
    문자열 입력에서의 동적메모리 할당
*/
int main() {
    SetConsoleOutputCP(65001);
    
    // 3명의 이름을 입력받으세요.

    char* names[3];
    char tmp[10+1];
    for (size_t i = 0; i < 3; i++)
    {
        scanf("%s", tmp);
        names[i] = (char*)malloc(strlen(tmp)+1);
        strcpy(names[i], tmp);
    }

    // 포인트배열을 이용하여 메모리를 할당하였을 경우는 배열의 주소값을 free 해야 한다.
    for (size_t i = 0; i < 3; i++)
    {
        free(names[i]);
    }
    
    return 0;
}