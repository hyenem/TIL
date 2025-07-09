#ifndef _SAMPLE_H_
#define _SAMPLE_H_
#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

template<typename T>
class Sample{
private :
    T x, y;
public:
    Sample(T a, T b);       
    void print();
};

#endif