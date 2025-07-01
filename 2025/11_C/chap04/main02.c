#include<stdio.h>
#include<stdlib.h>
// 관계연산자

int main() {
	int a = 10, b = 20, res;
	res = a > b;
	// 거짓은 0 , 0 이 아니면 참(1)
	printf("%d\n", res);

	printf("%d\n", a >= b);
	printf("%d\n", a < b);
	printf("%d\n", a <= b);
	printf("%d\n", a == b);
	printf("%d\n", a != b);
	printf("----------------------\n");
	//논리 연산자
	// && || !
	printf("%d\n", (a>9) && (b>19));
	printf("%d\n", (a < 9) && (b > 19));
	printf("%d\n", (a < 9) || (b > 19));
	printf("%d\n", (a < 9) || (b < 19));
	printf("%d\n", !(a < 9));

	return 0;
}
