#include<stdio.h>
#include<stdlib.h>
#include<string.h>
// 다(3)차원 배열의 배열 포인터

void print4(int arr[2][3][4]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 4; k++) {
                printf("%d ", arr[i][j][k]);
            }
            printf("\n");
        }
        printf("\n");
    }
    printf("----------------------\n");
}

void print5(int(*ap)[3][4]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 4; k++) {
                printf("%d ", ap[i][j][k]);
            }
            printf("\n");
        }
        printf("\n");
    }
    printf("----------------------\n");
}


// 다(3)차원 배열의 배열 포인터
int main() {
    

    int arr[2][3][4] = {
                            {
                                { 1, 2, 3, 4 },
                                { 5, 6, 7, 8 },
                                { 9, 10, 11, 12 }
                            },
                            {
                                { 13, 14, 15, 16 },
                                { 17, 18, 19, 20 },
                                { 21, 22, 23, 24 }
                            }
                       };

    int(*ap)[3][4];

    ap = arr;

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 4; k++) {
                printf("%d ", ap[i][j][k]);
            }
            printf("\n");
        }
        printf("\n");
    }
    printf("----------------------\n");
    // 배열로 받기
    print4(arr);
    // 배포로 받기
    print5(arr);
    

    return 0;
}
