#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

#define PI 3.141592
#define LIMIT 10
#define MSG "pass~~~"
#define ERR_PRINT printf("반지름이 너무 큽니다.\n")
#define SUM(a, b)((a)+(b))
#define MINUS(a, b)((a)-(b))

int main() {
    SetConsoleOutputCP(65001);
    
    double radius = 12, area;

    if(radius>LIMIT){
        ERR_PRINT;
    } else {
        area = radius * radius * PI;
        printf("area = %.2f (%s)\n", area, MSG);
    }

    int a = 10, b =- 5;
    printf("sum = %d\n", SUM(a, b));
    printf("minus = %d\n", MINUS(a, b));
    return 0;
}