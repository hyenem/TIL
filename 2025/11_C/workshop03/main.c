#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include"mylib.h"

int main() {

	Book books[10];

	int menu = 0;

	while (1) {
		printf("1:목록, 2:도서명검색, 3:입력, 4:수정, 5:삭제, 0:종료\n");
		scanf("%d", &menu);
		switch (menu) {
		case 1:
			func(printBook, books);
			break;
		case 2:
			func(findBook, books);
			break;
		case 3:
			func(insertBook, books);
			break;
		case 4:
			func(updateBook, books);
			break;
		case 5:
			func(deleteBook, books);
			break;
		case 0:
			printf("프로그램이 종료되었습니다.\n");
			exit(0);
		default:
			break;
		}
	}
	return 0;
}
