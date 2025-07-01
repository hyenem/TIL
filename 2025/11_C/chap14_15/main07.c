#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
// 포인터 배열을 받는 이중포인터 
void print(int** jumsu){
    printf("print jumsu sizeof = %d \n",sizeof(jumsu));
    printf("print jumsu =%u *jumsu =%u **jumsu =%u \n", jumsu, *jumsu , **jumsu);
    printf("print jumsu =%u *jumsu =%u **jumsu =%u \n", jumsu, jumsu[0] , jumsu[0][0]);

    printf("print jumsu =%u *jumsu =%u **jumsu =%u \n", jumsu, *jumsu , *(*(jumsu+2)+3));
}
int main() {
    SetConsoleOutputCP(65001);
    int a[] = {1,3,5};
    int b[] = {2,4,6,8};
    int c[] = {11,33,55,66,99};
    int* jumsu[3];
    jumsu[0] = a;
    jumsu[1] = b;
    jumsu[2] = c;
    
    print(jumsu);
    
    //char** pname = name;
    return 0;
}