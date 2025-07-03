/*
 * mylib.h
 */

#ifndef MYLIB_H_
#define MYLIB_H_

typedef struct {
	char name[50];
	int price;
	char author[50];
	char publisher[50];
} Book;

void insertBook(Book** books);
void printBook(Book** books);
void updateBook(Book** books);
void deleteBook(Book** books);
void findBook(Book** books);
void bookFree(Book** books);
void savetoFile(Book** books);
void loadFromFile(Book** books);
void func(void (*fp)(Book**), Book** books);

#endif  // MYLIB_H_ 
