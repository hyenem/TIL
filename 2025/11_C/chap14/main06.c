#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <string.h>

// void print(int* jumsu){
//     printf("print : %d", sizeof(jumsu)); //8
//     // printf("%d", jumsu[0]);
//     printf("%d %d", *jumsu, **jumsu);
// }
void print(int** pjumsu){
    printf("print : %d\n", sizeof(pjumsu)); //8
    printf("%u %u %u\n", pjumsu, *pjumsu, **pjumsu);
    printf("%u %u %u\n", pjumsu, pjumsu[0], pjumsu[0][0]);

    printf("%u %u %u \n", pjumsu, *pjumsu, *(*(pjumsu +2)+3));
}

int main() {
    SetConsoleOutputCP(65001);

    int* jumsu[3] = {(int[]){1, 3, 5}, (int[]){2, 4, 6, 8}, (int[]){10, 20, 30, 40, 50}};
    
    printf("main : %d\n", sizeof(jumsu)); //24
    // print(name);
    int** pjumsu = jumsu;
    print(pjumsu);

    return 0;
}