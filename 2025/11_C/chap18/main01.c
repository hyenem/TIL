#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main() {
    SetConsoleOutputCP(65001);
    
    FILE* wfp = fopen("test.txt", "a");
    if(wfp == NULL){
        printf("파일 쓰기 권한 실패\n");
        return -1;
    }

    fprintf(wfp, "%s", "파일에 문자열을 씁니다!!\n");

    printf("파일 쓰기 완료");
    fclose(wfp);

    return 0;
}