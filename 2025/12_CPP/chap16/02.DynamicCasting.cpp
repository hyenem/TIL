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

    Car* c = new Truck(20, 1000);
    // 다운캐스팅할떄는 virtual 붙은 가상함수가 있어야만함.
    // 없는 경우는 다운캐스팅할 의미가 없다는 뜻
    Truck* t = dynamic_cast<Truck*>(c);

    // Car* c1 = new Car(100);
    // Truck* t1 = dynamic_cast<Truck*>(c1);//error
    // if(t1==nullptr){
    //     cout << "dynamic_cast<Truck*>(c1) 캐스팅 실패" << endl;
    //     return 0;
    // }

    Truck* t2 = new Truck(10, 200);
    Car* c2 = t2;
    Car* c2 = dynamic_cast<Car*>(t2);
    if(c2!=nullptr){
        cout << "형변환 잘 됐습니다." << endl;
    }

    return 0;
}