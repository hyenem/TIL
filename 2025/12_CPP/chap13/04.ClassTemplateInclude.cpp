#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

/*
    템플릿 클래스를 include 할때는 .h 파일과 .cpp 파일을 모두 include 해야한다
    
*/
#include "Sample.h"
#include "Sample.cpp"

int main() {
    SetConsoleOutputCP(65001);
    
    Sample<int> s(10,5);
    s.print();
    return 0;
}