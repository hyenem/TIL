#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

/*
    합과 곱을 저장할 변수를  int 변수 하나를 사용하여 더하기 값과 곱하기 값을 구하세요
*/
 void recursive(int* arr, int len, int idx,int val){
    // basis part
    if(idx == len){
        printf("val = %d ",val);    
        return;
    }
    // inductive part (가지=> 경우의수 )
    recursive(arr, len, idx+1, val+arr[idx]);
    recursive(arr, len, idx+1, val*arr[idx]);
};
int main() {
    SetConsoleOutputCP(65001);
    int arr[] = {1,3,5};

    recursive(arr,sizeof(arr)/sizeof(arr[0]),0,1);


    return 0;
}