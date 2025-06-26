#include<stdio.h>
#include<stdlib.h>

// 형변환연산자
int main() {
	int a = 12, b = 10;
	double res;
	
	res = a / b;
	printf("res = %d\n", res);


	res = (double)a / (double)b;
	printf("res = %lf\n", res);

	a = (int)res;
	printf("(int)res = %.1lf 의 결과는 %d \n", res, a);
	return 0;
}
