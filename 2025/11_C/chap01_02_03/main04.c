/*
 * Main043.c
 *
 *  문자와 문자열 입력받기
 */
#include<stdio.h>
#include<stdlib.h>
#include <windows.h>
int main() {
	SetConsoleOutputCP(65001);
	char a;
	printf("문자를 입력하세요\n");
	scanf("%c", &a);
	printf("%c\n", a);

	char str[50];
	printf("문자열을 입력하세요\n");
	scanf("%s", str);
	printf("%s\n", str);
	return 0;
}

