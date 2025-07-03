#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

typedef struct{
    int age;
    char name[10+1];
} Person;

int main() {
    SetConsoleOutputCP(65001);
    
    FILE* fp = fopen("test.txt", "r");
    if(fp == NULL){
        printf("파일 읽기 권한 실패\n");
        return -1;
    }

    char str[100];
    Person p;

    fscanf(fp, "%d %s", &p.age, p.name);
    printf("%d %s", p.age, p.name);

    fclose(fp);

    return 0;
}