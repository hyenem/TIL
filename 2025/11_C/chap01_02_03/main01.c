#include <stdio.h>
#define MAX 10

/*
    ctrl + shift + b build
    ctrl + alt + n running
*/

/*   chcp 65001      // change cp mode 'UTF-8' 한글깨짐
    #include <windows.h>
    SetConsoleOutputCP(65001);
    으로 해결가능

    전처리기 : c -> i  define 등 전처리 (gcc -E test.c -o test.i)
    컴파일러 : i -> s  어셈블리로 생성  (gcc -S test.c)
    어셈블러 : s -> o  기계어로 생성    (gcc -c test.c)
    링커 : o -> exe    여러파일을 연결하여 실행파일로 생성
    gcc test.c -o main

    1. 전처리 단계 - 전처리기 (.i)
        #include, #define 등 #으로 시작하는 문법 사항이 적절히 전처리된 C 언어 '소스파일' 생성
    2. 컴파일 단계 - 컴파일러 (.s)
        C 언어 소스파일은 컴파일 과정을 거쳐 '어셈블리 소스 파일'이 됨
    3. 어셈블 단계 - 어셈블러 (.o)
        어셈블리 소스 파일은 어셈블 과정을 거쳐 '목적 파일'이 됨
    4. 링크 단계 - 링커 (.exe)
        목적 코드는 라이브러리와 링크되어 '실행 가능한 파일'이 됨
*/
#include <windows.h>
    
// int main(){
//     SetConsoleOutputCP(65001);
//     printf("Hello C !! %d \n",MAX);
//     return 0;
// }