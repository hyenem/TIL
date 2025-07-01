
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

int idx = 0;

void insertBook(char (*name)[50], int* price)
{
	printf("책이름을 입력하세요\n");
	scanf("%s", name[idx]);
	printf("책가격을 입력하세요\n");
	scanf("%d", &price[idx]);
	idx++;
}

void printBook(char (*name)[50], int* price)
{
	int i;

	printf("  책이름 \t\t 책가격\n");
	for (i = 0; i < idx; i++)
	{
		printf("[%d] %s \t %d \n", i + 1, name[i], price[i]);
	}
}

void updateBook(char (*name)[50], int* price)
{
	int i;
	char book[50];
	int _price;
	printf("수정할 책번호을 입력하세요\n");
	scanf("%d", &i);
	printf("수정할 책이름을 입력하세요\n");
	scanf("%s", book);
	printf("수정할 책가격을 입력하세요\n");
	scanf("%d", &_price);

	strcpy(name[i - 1], book);
	price[i - 1] = _price;
}

void deleteBook(char (*name)[50], int* price)
{
	int i;
	printf("삭제할 책번호을 입력하세요\n");
	scanf("%d", &i);

	strcpy(name[i - 1], name[idx - 1]);
	price[i - 1] = price[idx - 1];
	idx--;
}

void findBook(char (*name)[50], int* price)
{
	int i;
	char book[50];
	printf("검색할 책이름을 입력하세요\n");
	scanf("%s", book);
	for (i = 0; i < idx; i++)
	{
		if (!strcmp(name[i], book))
		{
			printf("  책이름 \t\t 책가격\n");
			printf("[%d] %s \t %d \n", i + 1, name[i], price[i]);
		}
	}
}

void funcExecute(void (*func)(char (*)[50], int*), char (*name)[50], int* price){
	func(name, price);
}