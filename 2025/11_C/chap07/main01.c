#include <stdio.h>
#include <stdlib.h>
#include <windows.h>


int add(int a, int b);
int minus(int a, int b);
int cross(int a, int b);
int division(int a, int b);

int main() {
    SetConsoleOutputCP(65001);
    int a = 10, b = 5, res = 0;
    // 함수의 호출부    

    res =  add(a,b);
    res =  cross(a,b);
    res =  minus(a,b);
    res =  division(a,b);
    printf("res = %d \n",res);
    return 0;
}


int add(int a, int b)/*함수의 선언부*/{
    // 함수의 구현부
    return a + b;
}

int minus(int a, int b)/*함수의 선언부*/{
    // 함수의 구현부
    return a - b;
}

int cross(int a, int b)/*함수의 선언부*/{
    // 함수의 구현부
    return a * b;
}

int division(int a, int b)/*함수의 선언부*/{
    // 함수의 구현부
    return a / b;
}
