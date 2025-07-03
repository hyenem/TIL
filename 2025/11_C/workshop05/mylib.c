#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include"mylib.h"
extern int N;
int bindex = 0;

void func(void (*fp)(Book**), Book** books) {
	fp(books);
};

void insertBook(Book** books) {
	
	books[bindex] = (Book*) malloc(sizeof(Book));

	printf("책이름을 입력하세요\n");
	scanf("%s", books[bindex]->name);
	printf("책가격을 입력하세요\n");
	scanf("%d", &books[bindex]->price);
	printf("책저자을 입력하세요\n");
	scanf("%s", books[bindex]->author);
	printf("출판사를 입력하세요\n");
	scanf("%s", books[bindex]->publisher);
	bindex++;

}

void printBook(Book** books) {
	int i;

	printf("  책이름 \t\t 책가격 \t\t 책저자 \t\t 출판사 \n");
	for (i = 0; i < bindex; i++) {
		printf("[%d] %s \t %d \t\t %s \t\t %s \n", i + 1, books[i]->name,
				books[i]->price, books[i]->author, books[i]->publisher);
	}
}

void updateBook(Book** books) {
	int i;
	char name[50];
	int price;
	char author[50];
	char publisher[50];

	printf("수정할 책번호을 입력하세요\n");
	scanf("%d", &i);
	printf("수정할 책이름을 입력하세요\n");
	scanf("%s", name);
	printf("수정할 책가격을 입력하세요\n");
	scanf("%d", &price);
	printf("수정할 책저자을 입력하세요\n");
	scanf("%s", author);
	printf("수정할 출판사를 입력하세요\n");
	scanf("%s", publisher);

	strcpy(books[i - 1]->name, name);
	books[i - 1]->price = price;
	strcpy(books[i - 1]->author, author);
	strcpy(books[i - 1]->publisher, publisher);
}

void deleteBook(Book** books) {
	int i;
	printf("삭제할 책번호을 입력하세요\n");
	scanf("%d", &i);

	strcpy(books[i - 1]->name, books[bindex - 1]->name);
	books[i - 1]->price = books[bindex - 1]->price;
	strcpy(books[i - 1]->author, books[bindex - 1]->author);
	strcpy(books[i - 1]->publisher, books[bindex - 1]->publisher);

	free(books[bindex - 1]);

	bindex--;

}

void findBook(Book** books) {
	int i;
	char book[50];
	printf("검색할 책이름을 입력하세요\n");
	scanf("%s", book);
	for (i = 0; i < bindex; i++) {
		if (!strcmp(books[i]->name, book)) {
			printf("  책이름 \t\t 책가격 \t\t 책저자 \t\t 출판사 \n");
			printf("[%d] %s \t %d \t %s \t %s \n", i + 1, books[i]->name,
					books[i]->price, books[i]->author, books[i]->publisher);

		}
	}

}

void bookFree(Book** books) {
	int i;
	for (i = 0; i < bindex; i++) {
		free(books[i]);
	}
}

void loadFromFile(Book** books) {
	int res=0;

	FILE* fd = fopen("book.txt", "r");
	if (fd == NULL) {
		printf("File 읽기 실패\n");
		return;
	}

	while (1) {
		Book* pb = (Book*) malloc(sizeof(Book));
		res = fscanf(fd,"%s %d %s %s", pb->name, &pb->price,
				pb->author, pb->publisher);
		if(res == EOF){
			break;
		}
		books[bindex]=pb;
		bindex++;

	}
	fclose(fd);
}

void savetoFile(Book** books) {
	int i;
	FILE* fd = fopen("book.txt", "w+");
	if (fd == NULL) {
		printf("File 쓰기 실패\n");
		return;
	}
	for (i = 0; i < bindex; i++) {
		fprintf(fd, "%s %d %s %s\n", books[i]->name, books[i]->price,
				books[i]->author, books[i]->publisher);
	}
	fclose(fd);
}
