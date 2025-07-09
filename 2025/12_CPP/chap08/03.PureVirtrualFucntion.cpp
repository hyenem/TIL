#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
class First{
public :
    virtual void print() = 0;
};
class Second : public First{
public :
    void print(){
        cout<<"second"<<endl;
    }
};
int main() {
    SetConsoleOutputCP(65001);

    Second s;

    return 0;
}