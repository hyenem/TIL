
#include<stdio.h>
#include<stdlib.h>

int main06() {
	int rank;
	int jumsu;
	printf("정수를 입력하세요 [0 ~ 9] \n");
	scanf("%d", &rank);

	switch (rank) {
	case 1:
		jumsu = 100;
		break;
	case 2:
		jumsu = 90;
		break;
	case 3:
		jumsu = 80;
		break;
	case 4:
		jumsu = 70;
		break;
	case 5:
		jumsu = 60;
		break;
	default:
		jumsu = 50;
		break;
	}

	printf("당신의 점수는 %d 입니다.", jumsu);
	return 0;

}
