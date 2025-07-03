#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
/*
    열거형
*/
enum season{
    SPRING, SUMMER, FALL=5, WINTER
};

int main() {
    SetConsoleOutputCP(65001);
    printf("%d %d %d %d\n", SPRING, SUMMER, FALL, WINTER);

    enum season s;
    s = SUMMER;
    char* str = NULL;
    switch(s){
        case SPRING:
            str = "flower";
        break;
        case SUMMER:
            str = "swimming";
        break;
        case FALL:
            str = "mountain";
        break;
        case WINTER:
            str = "ski";
        break;
    }
    printf("%s\n", str);
    return 0;
}