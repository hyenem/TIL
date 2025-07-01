#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

/*
    recursive fucntion
*/
void recursive(int i, int sum){
    // basis part
    if(i>10){
        printf("sum = %d \n",sum);    
        return;
    }
    // logic part
    sum += i;
    // inductive part
    recursive(i+1,sum);
}

int main() {
    SetConsoleOutputCP(65001);
    
    // 1 ~ 10 더한다
    int i = 1, sum = 0;
    // for(i=1;i<=10;i++){
    //     sum += i;
    // }
    recursive(i,sum);   
    printf("sum = %d \n",sum);
    return 0;
}