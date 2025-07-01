#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
 /*
    1 ~ 10 더 하세요
    단 재귀함수의 인자를 하나만 사용하세요
 */
int recursive(int i){
    if(i == 1 ) return i;

    return recursive(i-1)+i;
}

int main() {
    SetConsoleOutputCP(65001);
    
    // 1 ~ 10 더한다
    int i = 10, sum = 0;
  
    sum = recursive(i);   
    printf("sum = %d \n",sum);
    return 0;
}