
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int i;   // 초기식
	int sum=0;

	for (i = 1; i <= 100; i++) {
		if(i%2 == 0){
			sum += i;
		};
	}
	printf("1 ~ 100 의 합은 = %d\n", sum);

	return 0;
}
