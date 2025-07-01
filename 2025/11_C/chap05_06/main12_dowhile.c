
#include <stdio.h>
#include <stdlib.h>

int main12(void) {
	int res;
	int i = 1;   // 초기식
	do {
		// 조건식
		res = 2 * i;
		printf("2 * %d = %d\n", i, res);
		i++; //증감식

	} while (i <= 9);

	return 0;
}
