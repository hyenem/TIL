#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main() {
    SetConsoleOutputCP(65001);
    
    FILE* fp = fopen("test.txt", "r");
    if(fp == NULL){
        printf("파일 읽기 권한 실패\n");
        return -1;
    }

    char str[100];

    while(fscanf(fp, "%s", str) != EOF){
        printf("%s", str);
    }

    fclose(fp);

    return 0;
}