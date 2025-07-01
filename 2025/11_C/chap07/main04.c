#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

/*
    arr 배열의 요소값의 합과 곱을 구하세요
*/
void recursive(int* arr, int len, int idx,int sum, int cross){
    if(idx == len){
        printf("sum = %d, cross = %d ",sum, cross);    
        return;
    }
    printf("%d ",arr[idx]);
    recursive(arr, len, idx+1, sum+arr[idx], cross * arr[idx]);
};

int main() {
    SetConsoleOutputCP(65001);
    int arr[] = {1,3,5,7};

    recursive(arr,sizeof(arr)/sizeof(arr[0]),0,0,1);


    return 0;
}