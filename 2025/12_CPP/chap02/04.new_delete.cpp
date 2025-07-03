#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

int main() {
    SetConsoleOutputCP(65001);

    // c style
    // 동적 선언
    char* str = (char*)malloc(sizeof(char)*20);
    strcpy(str, "i'm happy");
    printf("%s\n", str);
    free(str);

    //cpp style
    str = new char[20];
    strcpy(str, "i'm happy too");
    str[20] = 'c';
    cout << str << endl;
    // 배열을 delete 할 떄는 []를 붙입니다.
    delete[] str;

    return 0;
}