#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
/*
    다차원 배열
*/ 
int main() {
    SetConsoleOutputCP(65001);
    
    int jumsu[2][3] = {{100,90,80},{70,60,50}};
    //jumsu[3]
    printf("%u %u %u\n",jumsu,jumsu[0],jumsu[0][0]);

    int* p = (int*)jumsu;
    printf("%d %d %d\n",*p, *(p+3), p[3]);

    
    printf("%d %d %d\n",sizeof(jumsu),sizeof(jumsu[0]),sizeof(jumsu[0][0]));

    for (size_t i = 0; i < sizeof(jumsu)/sizeof(jumsu[0]); i++){
        for (size_t j = 0; j < sizeof(jumsu[0])/sizeof(jumsu[0][0]); j++){
            printf("%d ",jumsu[i][j]);
        }
        printf("\n");
    }
    

    return 0;
}