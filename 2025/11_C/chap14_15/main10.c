#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
	배열 포인터
*/

int main09() {
	// 일차원배열
	int arr[5] = {1,2,3,4,5};
	printf("%u %u %u %u\n", arr, &arr, arr + 1, &arr + 1);

	// 이차원배열   
	int arr2[2][2] = { {1,3},{5,7} };
	printf("%u %u %u %u\n", arr2, &arr2, arr2 + 1, &arr2 + 1);
	printf("%u %u %u %u\n", arr2, &arr2, arr2[1], &arr2[1]);


	// 배열포인터
	int(*p)[2] = arr2;
	printf("%u %u %d %d %d \n", p, *p, **p, p[1][1], *(*(p + 1) + 1));
	
	// 배열포인터의 주소값을 이중포인터로 지정하는 것은 위험하다
	int** pp = &p;
	// pp+1 은 1차원 포인터로 인식하고 포인트크기만큼 이동한다
	// 배열포인터를 이중포인터로 지정해도 이중포인터를 2차원 배열처럼쓰지 못한다
	// 되는 것처럼 보이나
	printf("%u %u %d %u %u %u\n", pp, *pp, **pp, pp+1, *((*pp) + 2), *((*pp) + 2));
	printf("-------------에러 난다--------------------------\n");
	printf("%d %d \n", pp[0][0], pp[1][1]);
	return 0;
}