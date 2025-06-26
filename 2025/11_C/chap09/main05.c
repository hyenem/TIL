#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

int main() {
    SetConsoleOutputCP(65001);

    printf("%s %u %u %c %c %c \n", "apple", "apple", "apple"+1, *"apple", *("apple")+1, *("apple"+1));

    // 입력시에 배열을 선언하여 입력을 받으면 수정이 가능ㅎ다ㅏ.
    char input[80];

    return 0;
}
