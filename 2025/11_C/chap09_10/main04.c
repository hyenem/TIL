#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
 
void change(const int* arr){

};
int main() {
    SetConsoleOutputCP(65001);
    // 문자배열로 선언
    char arr[] = "apple";
    char arr2[] = "apple";
    printf("%s\n",arr);
    printf("%d %d\n",arr, arr2);

    char* parr = arr;
    parr[0] = 'b';

    printf("%s\n",parr);
    // 문자포인터변수로 선언
    const char* parr2 = "banana";
    printf("%s\n",parr2);
    // 문자를 변경할수 없다  
    // parr2[0] = 'c';
    // printf("%s\n",parr2);

    char* parr3 = "banana";

    printf("%u %u\n",parr2, parr3);

    return 0;
}