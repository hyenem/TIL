
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include "mylib.h"

void (*table[5])(char (*)[50], int*) = {printBook, findBook, insertBook, updateBook, deleteBook};

int main()
{
	SetConsoleOutputCP(65001);
	char name[10][50];
	int price[10];
	int menu = 0;

	while (1)
	{
		printf("1:목록, 2:도서명검색, 3:입력, 4:수정, 5:삭제, 0:종료\n");
		scanf("%d", &menu);
		if(!menu){
			printf("프로그램이 종료되었습니다.\n");
			exit(0);
		} else {
			funcExecute(table[menu-1], name, price);
		}
	}
	return 0;
}
