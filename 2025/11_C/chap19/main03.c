#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main() {
    SetConsoleOutputCP(65001);
    printf("날짜 : %s , 시간 : %s\n", __DATE__, __TIME__);
    printf("파일 : %s , 함수 : %s , 라인 : %d \n", __FILE__, __FUNCTION__, __LINE__);
    return 0;
}