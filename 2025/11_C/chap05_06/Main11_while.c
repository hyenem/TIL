
#include <stdio.h>
int main() {
	int i = 1, sum = 0, n;
	printf("양의 정수 n을 입력하세요: ");
	scanf("%d", &n);

	while (1) {

		sum += i;
		i++;
		if(i == n+1){
			break;
		}
		if (i == 4) {
			// 6을 빼고 계산
			i += 2;
			continue;
		}
	}
	printf("합은 %d\n", sum);

	return 0;
}
