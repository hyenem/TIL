#include<stdio.h>
#include<stdlib.h>


int main05() {

    int c = 0; // 0000
    int flag = 1; // 0001

    // bit 자리 바꾸기
    c = c | (flag << 2);
    printf("c | (flag << 2) = %d\n", c);

    // 자리수 값 확인하기
    c = 5;// 101
    flag = 1 << 0; //001
    printf("c&flag = %d\n", c & (flag));

    flag = 1 << 0;// 0000
    if ((c & flag) > 0) {
        printf("1<<0 자리수의 값이 1 입니다 ");
    }
    else {
        printf("1<<0 자리수의 값이 0 입니다 ");
    }
	return 0;
}