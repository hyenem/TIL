#include <stdio.h>


int main(void) {
	int res;
	int i = 1;   // 초기식
	int j = 2;

	for(j=2;j<=9;j++) {
		if(j== 3 || j == 7){
			// continue;
			goto L;

		}
		for (i = 1; i <= 9; i++) {
			res = j * i;
			printf("%d * %d = %d\n",j, i, res);

		}
	}
L:
	printf("end of main");

	return 0;
}
