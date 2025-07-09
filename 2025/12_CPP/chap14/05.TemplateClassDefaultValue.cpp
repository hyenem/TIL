#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
template<class T=int, int len=7>
class SampleArray{
private :
    T arr[len];
public :
    T& operator[](int idx){
        return arr[idx];
    }
};
int main() {
    SetConsoleOutputCP(65001);

    SampleArray<> arr;
    arr[0] = 1;
    arr[1] = 3;
    arr[2] = 5;

    cout<< arr[0]<<", "<< arr[1] << ", " << arr[2] << endl;
    SampleArray<double, 4> arr2;
    return 0;
}