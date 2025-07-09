#include "Sample.h"

// sample.cpp 
template<typename T>
Sample<T>::Sample(T a, T b):x(a),y(b){};

template<typename T>
void Sample<T>::print(){
    cout << x <<","<< y << endl;
}