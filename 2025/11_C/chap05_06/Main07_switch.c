#include<stdio.h>
#include<stdlib.h>
// 계산기 프로그램
// 두수를 입력받아 사칙연산(+ - * / %) 를 구하는 프로그램
// 입력 3 + 5
// 출력 3 + 5 = 8

int main07() {
	int op1, op2, result; // 입력받을 두 정수 변수
	char op;
	//int i = 0;

	while (1) {
		printf("계산할 값을 입력하세요 ex) 3 + 4\n");
		//i = i+1;
		//i+=1;
		//i++;
		printf("종료시 0 0 0 을 입력하세요\n");
		scanf("%d %c %d", &op1, &op, &op2);

		if(op1 == 0 && op == '0' && op2 == 0){
			printf("프로그램이 종료되었습니다.\n");
			break;
		}

		switch (op) {
		case '+':
			result = op1 + op2;
			printf("%d %c %d = %d\n", op1, op, op2, result);
			break;
		case '-':
			result = op1 - op2;
			printf("%d %c %d = %d\n", op1, op, op2, result);
			break;
		case '*':
			result = op1 * op2;
			printf("%d %c %d = %d\n", op1, op, op2, result);
			break;
		case '/':
			result = op1 / op2;
			printf("%d %c %d = %d\n", op1, op, op2, result);
			break;
		case '%':
			result = op1 % op2;
			printf("%d %c %d = %d\n", op1, op, op2, result);
			break;
		default:
			printf("연산자를 잘못 입력하셨습니다.\n");
			break;
		}

	}
	return 0;
}

