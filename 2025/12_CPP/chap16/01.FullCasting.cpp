#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

class Car{
private:
    int fuel;
public:
    Car(int f) : fuel(f) {}
    void showFuel() {
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

    Car* c = new Truck(100, 2000);
    c->showFuel();

    Truck* t = (Truck*)c;
    t->showState();

    delete c;
    return 0;
}