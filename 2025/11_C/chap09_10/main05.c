#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
 
int main() {
    SetConsoleOutputCP(65001);
    
    printf("%s %u %u %c %c %c", "apple", "apple", "apple"+1,*"apple", *("apple")+1, *("apple"+1));

    // 입력시에 배열을 선언하여 입력을 받으면 수정이 가능하다
    char input[80];
    scanf("%s", input);
    printf("%s\n",input);

    char* p = input;
    scanf("%s", p);
    printf("%s\n",p);
    

    return 0;
}