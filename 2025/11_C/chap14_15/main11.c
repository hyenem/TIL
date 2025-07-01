#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
/*
    함수 포인터 변수
        정의 : 함수의 주소를 저장하는 변수
        형식 : 리턴타입 (*변수명)(인자타입)
*/
int sum(int a, int b){
    return a+b;
}
int minus(int a, int b){
    return a-b;
}
int funcExecute(int (*fp)(int a, int b), int a, int b){
    int res = fp(a, b);
    return res;
}

int main() {
    SetConsoleOutputCP(65001);

    printf("%u\n", sum);
    
    int (*fp)(int, int);

    // fp = sum;
    // printf("%u\n", fp(4,3));

    // fp = minus;
    // printf("%u\n", fp(4, 3));
    
    printf("%u\n", funcExecute(sum, 4, 3));
    printf("%u\n", funcExecute(minus, 4, 3));

    return 0;
}