
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include"mylib.h"
int N = 10;
extern int index;
int main() {
	Book* books[10];
	// Book** books = (Book**)malloc(sizeof(Book*)*N);
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
			/*if (index == N) {
				books = realloc(books, sizeof(Book*) * N * 2);
				if (books == NULL) {
					printf("메모리 할당 실패\n");
					exit(0);
				}
				N *= 2;
			}*/
			func(insertBook, books);
			break;
		case 4:
			func(updateBook, books);
			break;
		case 5:
			func(deleteBook, books);
			break;
		case 0:
			func(bookFree, books);
			printf("프로그램이 종료되었습니다.\n");
			exit(0);
		default:
			break;
		}
	}
	free(books);
	return 0;
}
