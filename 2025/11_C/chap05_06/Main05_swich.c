
#include<stdio.h>
#include<stdlib.h>

int main05() {
	int a;
	printf("정수를 입력하세요 [0 ~ 9] \n");
	scanf("%d", &a);

	switch (a) {
	case 0:
		printf("입력하신 값은 0 입니다.\n");
		break;
	case 1:
		printf("입력하신 값은 1 입니다.\n");
		break;
	case 2:
		printf("입력하신 값은 2 입니다.\n");
		break;
	case 3:
		printf("입력하신 값은 3 입니다.\n");
		break;
	case 4:
		printf("입력하신 값은 4 입니다.\n");
		break;
	default:
		printf("default 입니다.\n");
		break;
	}
	return 0;
}

