#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

/*
    class template
*/
// sample.h
template<typename T>
class Sample{
private :
    T x, y;
public:
    Sample(T a, T b);       
    void print();
};

// sample.cpp 
template<typename T>
Sample<T>::Sample(T a, T b):x(a),y(b){};

template<typename T>
void Sample<T>::print(){
    cout << x <<","<< y << endl;
}

int main() {
    SetConsoleOutputCP(65001);
    
    Sample<int> s(10,5);
    s.print();
    return 0;
}