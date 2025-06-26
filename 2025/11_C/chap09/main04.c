#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main() {
    SetConsoleOutputCP(65001);
    
    char arr[] = "apple";
    printf("%s \n", arr);

    char* parr = arr;
    parr[0] = 'b';
    printf("%s \n", parr);

    char* parr2 = "banana";
    // const char* parr2 = "banana";
    printf("%s \n", parr2);

    // 문자를 변경할 수 없다.
    // 리터럴 풀에 선언되기 때문!
    // parr[0] = 'c';
    // printf("%s \n", parr2);

    char* parr3 = "banana";
    printf("%u %u \n", parr2, parr3);

    return 0;
}