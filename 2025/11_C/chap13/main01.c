#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include "main02.h"
/*
    변수의 생명주기

    지역변수 : scope 안에서 선언되어지는 변수
            소멸시점 : scope 이 끝나면 소멸된다
            활성영역 : scope 안에서 사용되어 진다 다만 상위 scope 에서 선언되어진 변수는 하위scope 에서 사용할수 있다
                        만약 상위와 하위에서 동일한 변수명이 선언되어 진다면 실행스코프의 변수가 우선선택됩니다
    전역변수 : scope 밖에서 선언되어지는 변수
            소멸시점 : 프로그램이 끝나면 소멸된다
            활성영역 : 프로그램전체
    정적전역변수
        자신의 .c 파일에서만 전역으로 작동하는 변수
    정적지역변수
        자신이 선언되어진 함수가 끝나도 사라지지 않는 지역변수
    레지스터변수
        메모리가 아니고 레지스트영역에 선언되어지는 변수 입니다
        장점 : 속도는 대단히 빠르나 레지스트영역이 작아서 레지스트변수로 선언한다고 그 영역으로 올라간다는 보장이 없습니다
        단점 : 레지스트변수는 포인터변수로 가르킬수 없습니다

*/
// 전역변수
static int ga = 20;

void func1();
int* func2();
void func3(){
    register int r = 10;
    //int * p = &r;
}

int main() {
    SetConsoleOutputCP(65001);
    // 지역변수
    int  a = 10;
    //int ga = 30;
    printf("a = %d , ga = %d\n",a, ga);
    //func1();
    //int* p = func2();
    //int res = *p + 1;
    // func2();
    // func2();
    // func2();
    // func2();
    print();
    return 0;
}

void func1(){
    printf("ga = %d\n",ga);
}

int* func2(){
    // 정적지역변수 
    static int a = 10;
    int b = 20;
    printf("a = %d \n",a++);    
    return &a;
};