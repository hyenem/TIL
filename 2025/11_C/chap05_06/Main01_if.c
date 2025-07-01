
#include <stdio.h>
#include <stdlib.h>
int main01() {
	int a, b;
	printf("두 정수를 입력하세요\n");
	scanf("%d %d", &a, &b);
	if (a == b) {
		printf("%d is equal to %d\n", a, b);
	}
	if (a > b) {
		printf("%d is greater than %d\n", a, b);
	}
	if (a < b) {
		printf("%d is less than %d\n", a, b);
	}
	return 0;
}

