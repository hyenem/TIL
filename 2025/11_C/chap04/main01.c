#include<stdio.h>
#include<stdlib.h>

int main() {
	// 대입연산자
	int a = 10;
	a = a + 5;
	a += 5;
	a = a - 5;
	a -= 5;
	a *= 5;
	a /= 10;
	a = a + 1;
	
	int b = 20;
	a = a + b;
	a += b;
	a = a - b;
	a -= b;
	a *= b;
	a /= b;

	// 나머지 연산
	a = a % b;

	// 전치 후치
	a = 10;
	b = 5;
	b =  b++ + ++a;
	printf("b = %d\n",b);

	++a;
	++a;
	a++;
	a--;

	a = 1;
	//++(++a);
	// 후치 단항 증감연산자는 연속적으로 되지 안는다
	//a++++;
	printf("%d\n",a);

	a = 10;
	b = ++a;
	printf("a = %d b = %d\n",a, b);
	a = 10;
	b = a++;
	printf("a = %d b = %d\n", a, b);

	return 0;
}
