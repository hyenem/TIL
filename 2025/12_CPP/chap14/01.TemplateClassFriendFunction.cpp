#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
/*
    template 클래스 에서 friend 함수 선언하기
*/ 
template<class T>
class Sample;   // 전방 선언

template<class T>
Sample<T>& operator+(Sample<T>& s1, Sample<T>& s2);

template<class T>
class Sample {
private:
    T x, y;
public:
    friend Sample<T>& operator+<>(Sample<T>& s1, Sample<T>& s2);
    Sample(T a, T b);
    void print();
};

template<typename T>
Sample<T>::Sample(T a, T b):x(a), y(b){}

template<typename T>
void Sample<T>::print(){
    cout << x <<","<< y << endl;
}

template<class T>
Sample<T>& operator+(Sample<T>& s1, Sample<T>& s2) {
    s1.x += s2.x;
    s1.y += s2.y;
    return s1;
}
int main() {
    SetConsoleOutputCP(65001);
    
    Sample<int> s1(10, 5);
    Sample<int> s2(20, 10);
    s1+s2;
    s1.print();
    return 0;
}