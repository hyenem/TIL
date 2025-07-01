#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
// powerset
 void recursive(int* arr, int len1, int* sel,int len2, int idx, int k){
    //basis part
    if(idx == len1){ // 원하는 만큼 다 선택했다
        if(k == 2){
            for (size_t i = 0; i < len2; i++)
            {
                if(sel[i]==1)
                    printf("%d ",arr[i]);
                else{

                }    
               
            }
            printf("\n ");
        }
        return;
    }

    // 선택하는 경우
    sel[idx] = 1;
    recursive(arr, len1, sel, len2, idx+1, k+1);
    
    // 선택하지 안는 경우
    sel[idx] = 0;
    recursive(arr, len1, sel, len2, idx+1, k);
};
int main() {
    SetConsoleOutputCP(65001);

    int arr[] = {1,3,5};
    int sel[] = {0,0,0};
    int len1 = sizeof(arr)/sizeof(arr[0]);
    int len2 = sizeof(sel)/sizeof(sel[0]);
    
    recursive(arr,len1, sel, len2, 0, 0);


    return 0;
}