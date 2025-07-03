#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

static int ga = 10;

void print(){
    static int ga = 20;
    printf("%d\n", ga++);
}

int main() {
    SetConsoleOutputCP(65001);
    
    // 지역변수
    int r = 10;

    printf("%d\n", r);

    print();
    print();
    print();

    return 0;
}