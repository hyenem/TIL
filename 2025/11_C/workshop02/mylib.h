
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

extern int idx;
void insertBook(char (*name)[50], int* price);
void printBook(char (*name)[50], int* price);
void updateBook(char (*name)[50], int* price);
void deleteBook(char (*name)[50], int* price);
void findBook(char (*name)[50], int* price);

void funcExecute(void (*)(char (*)[50], int*), char (*)[50], int*);