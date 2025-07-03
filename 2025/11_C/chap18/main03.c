#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
typedef struct {
    int age;
    char name[10+1];
} Person;

int main() {
    SetConsoleOutputCP(65001);

    FILE* wfp = fopen("test.txt", "w");
    if(wfp == NULL){
        printf("파일 쓰기 권한 실패\n");
        return -1;
    }

    Person p = {9, "둘리"};
    fprintf(wfp, "%d %s ", p.age, p.name);

    printf("파일 쓰기 완료");
    fclose(wfp);

    return 0;
}