#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
/*
    탬플릿클래스의 특수화
*/
template<class T>
class Sample{
private :
    T data;
public :
    Sample(T a):data(a){}
    int getSize(){return sizeof(T);}
};
template<>
class Sample<char*>{
private :
    char* data;
public :
    Sample(char* a): data(a){}
    int getSize(){return strlen(data);}
};
int main() {
    SetConsoleOutputCP(65001);

    Sample<int> s1(10);
    cout << s1.getSize() << endl;

    char name[20+1] = "scsa";
    Sample<char*> s2(name);
    cout << s2.getSize() << endl;

    return 0;
}