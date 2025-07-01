#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// 문자열 관련 함수

int main06() {
	char name1[] = "홍길동";
	char name2[] = { 'h','o','n' ,'g','\0' };
	char name3[] = "zong";
	char name4[20];
	printf("% d \n", strlen(name2));
	printf("% d \n", strlen(name1)); //한글은 2개씩 카운트
	printf("% d \n", strcmp(name2, name3)); // 같으면 : 0 , 1, -1
	printf("% s \n", strcpy(name4, name2));
	printf("% s \n", strcat(name4, " hi"));
	printf("% p \n", strchr(name4, 'h')); // 주소가 리턴이 된다
	return 0;
}