#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
 /*
    1 ~ 10 더하고, 곱하세요
    단 재귀함수의 인자를 하나만 사용하세요
    더한값과 곱한값중 작은값을 리턴으로 받기
 */
int dp[10]={0,0,0,0,0,0,0,0,0,0};
int recursive(int i){
    if(i ==1) return 1;
    if(dp[i]>0) return dp[i];
    return dp[i] = recursive(i-1)+i < recursive(i-1)*i?recursive(i-1)+i:recursive(i-1)*i;
}

int main() {
    SetConsoleOutputCP(65001);
    
    // 1 ~ 10 더한다
    int i = 10, sum = 0;
  
    sum = recursive(i);   
    printf("sum = %d \n",sum);
    return 0;
}