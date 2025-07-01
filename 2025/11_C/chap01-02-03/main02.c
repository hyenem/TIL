#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#define MAX 100
#define PI 3.141592
/*
    
	short		16bit		2byte
	int			32bit		4
	long		32bit		4
	long long	64bit		8

	float					4byte
	double					8
	long double				8

	char					1
	------------------------------
	%d
	%f
	%lf (long float)
	%c
	%s
	%o (8진수)
	%x (16진수)
	%u 부호없는 10진수


*/
int main() {
    SetConsoleOutputCP(65001);
    char a1 = 'B';
	printf("%c \n", a1);
	printf("%d \n", a1);
	printf("%d \n", 'A');
	printf("%d \n", 'a');

	printf("%d\n", MAX);
	printf("%lf\n", PI);
	printf("%lf\n", 3.4f);
	printf("%lf\n", 3.4);
	printf("%f\n", 3.4);
	printf("%x\n", 0xf);

	printf("%d\n", sizeof(int));

	unsigned int b;
	b = -1;

	printf("%u", b);
	return 0;
}