
// console 로부터 값을 입력받는 프로그램
// fflush 사용공부
#include<stdio.h>
#include<stdlib.h>
#include <windows.h>
int main() {
	SetConsoleOutputCP(65001);
	int a;
	char c;
	printf("숫자를 입력하세요\n");
	scanf("%d", &a);
	// fflush(stdin); //이제 이거 안되요 표준 아님
	while (getchar() != '\n'); // 끝의 세미콜론 주의!!

	printf("문자를 입력하세요\n");
	scanf("%c", &c);

	printf("숫자 : %d\n", a);
	printf("문자 : %c\n",c);
	return 0;
}

