
#include<stdio.h>
#include<stdlib.h>
#include <windows.h>
int main06() {
	SetConsoleOutputCP(65001);
	// const 변수의 상수화
	int a = 10;
	a = 20;
	// 선언과 초기화
	const int b = 20;
	// 값변경 불가
	// b = 30;

	return 0;
}
