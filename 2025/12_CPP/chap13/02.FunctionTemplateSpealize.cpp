#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

template <typename T> 
T Max(T a, T b){
    cout << "템플릿함수 Max T = " ;
    return a > b ? a : b;
}
// specialized
template<>
string Max(string s1, string s2){
    cout << "템플릿함수 특수화 string " ;        
    return s1.length() > s2.length()? s1 : s2;
}


int main() {
    SetConsoleOutputCP(65001);
    int a = 10, b = 5;
    cout << Max<int>(3,5) << endl;     
    cout << Max<double>(3,5) << endl;     

    cout << Max<string>("ssafy","scsa") << endl;
    return 0;
}