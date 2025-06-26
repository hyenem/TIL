#include<stdio.h>
#include<stdlib.h>


int main() {
	// 콤마 연산자
	int a = 12, b = 10;
	int res;

	res = (++a , b++);
	printf("a = %d, b = %d, res = %d\n",a,b, res);

	// 조건 연산자
	a = 10, b = 20;
	res = a > b ? a : b;
	printf("a = %d, b = %d, res = %d\n", a, b, res);

	// 비트 연산자
	a = 2, b = 4;
	printf("%d & %d = %d\n", a, b, a & b);
	printf("%d | %d = %d\n", a, b, a | b);
	printf("%d ^ %d = %d\n", a, b, a ^ b); // 서로 다를때만 참
	a = 1;
	printf("~%d = %d\n", a,  ~a);
	a = 1;
	printf("%d << 1 = %d\n", a, a << 1);
	printf("%d >> 1 = %d\n", a, a >> 1);

	// 연산자 우선순위
	a = 1;
	res = ++a * 3;
	//  3   1 2       
	printf("a = %d, res = %d\n", a, res);
	return 0;
}
