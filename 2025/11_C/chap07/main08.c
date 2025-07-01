#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
// 순열 
void recursive(int arr[], int len1, int sel[], int len2, int idx, int v[]){
     if(idx == len2){ // 원하는 만큼 다 선택했다
        for (size_t i = 0; i < len2; i++)
        {
           printf("%d ",sel[i]);
        }
        printf("\n ");
        
        return;
    }
    int i = 0;
    for(i=0;i<len1;i++){
        
        if(v[idx] == 0){
            v[idx] = 1;
            sel[idx]=arr[i];
            recursive(arr, len1, sel, len2, idx+1,v);
            v[idx] = 0;
        }
    }
    
    // if(v[0] == 0){
    //     v[0] = 1;
    //     sel[idx]=arr[0];
    //     recursive(arr, len1, sel, len2, idx+1,v);
    //     v[0] = 0;
    // }

    // if(v[1] == 0){
    //     v[1] = 1;
    //     sel[idx]=arr[1];
    //     recursive(arr, len1, sel, len2, idx+1,v);
    //     v[1] = 0;
    // }

    // if(v[2] == 0){
    //     v[2] = 1;
    //     sel[idx]=arr[2];
    //     recursive(arr, len1, sel, len2, idx+1,v);
    //     v[2] = 0;
    // }
    
}

int main() {
    SetConsoleOutputCP(65001);
    
    int arr[] = {1,3,5};
    int sel[2];
    int len1 = sizeof(arr)/sizeof(arr[0]);
    int len2 = sizeof(sel)/sizeof(sel[0]);
    int v[]={0,0,0};
    

    recursive(arr, len1, sel, len2, 0, v);

   
    return 0;
}