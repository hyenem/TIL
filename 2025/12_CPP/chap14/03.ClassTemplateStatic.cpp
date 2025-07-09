#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

template<class T>
class Sample{
private :
    T a;
    static T b;
public :
    Sample(T a):a(a){}
    void print(){
        cout << a++ << endl;
    }
    void print2(){
        cout << b++ << endl;
    }
};

template<class T>
T Sample<T>::b = 1;

int main() {
    SetConsoleOutputCP(65001);

    Sample<int> s1(1);
    s1.print2();
    s1.print2();
    s1.print2();
    
    Sample<int> s2(1);
    s2.print2();

    Sample<double> s3(1);
    s3.print2();
    s3.print2();

    return 0;
}