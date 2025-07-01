#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
 
int main() {
    SetConsoleOutputCP(65001);
    char input[10+1]={'0'};
    const char* pinput = "hong";

    // scanf("%s", input);
    // printf("%s",input);

    scanf("%s", pinput);
    printf("%s",pinput);
    return 0;
}