#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

class Car{
private:
    int fuel;
public:
Car(int f) : fuel(f) {}
    virtual void showFuel() {
        cout << "Fuel: " << fuel << endl;
    }
};
class Truck : public Car {
private:
    int weight;
public:
    Truck(int f, int w) : Car(f), weight(w) {}
    void showState(){
        showFuel();
        cout << "Weight: " << weight << endl;
    }
};

int main() {
    SetConsoleOutputCP(65001);

    // c style
    int a = 10, b = 4;
    double res = (double)a/(double)b;
    cout << res << endl;
    
    // cast 연산자
    res = static_cast<double>(a)/static_cast<double>(b);
    cout << res << endl;

    int* p = &a;
    float* fp = (float*)p;  //가능하지만 위험하다
    // static_cast 를 사용하면 캐스팅에 문제가 있다고 판단하여 캐스팅이 되지 않는다.
    // float* fp1 = static_cast<float*>(p);

    // 상속 관계만 확인하고 가상함수 존재 여부와 상관없이 형변환한다.
    Car* c = new Car(20);
    Truck* t = static_cast<Truck*>(c);

    return 0;
}