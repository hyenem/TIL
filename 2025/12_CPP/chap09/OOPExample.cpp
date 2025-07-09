#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

class Animal{
public :
    virtual void breath()=0;
    void bark(){
        cout << "소리냅니다" << endl;
    }
};
class Dog : virtual public Animal{
public :
    virtual void breath(){
        cout << "개가 숨을 쉽니다" << endl;
    }
    void bark(){
        cout << "개가 짖습니다" << endl;
    }
};
class Bird : virtual public Animal{
public :
    virtual void breath(){
        cout << "새가 숨을 쉽니다" << endl;
    }
    void fly(){
        cout << "새가 날아다닙니다" << endl;
    }
};
class Human : virtual public Animal{
public :
    virtual void breath(){
        cout << "사람이 숨을 쉽니다" << endl;
    }
};
class Superman : virtual public Human{
public :
    virtual void breath(){
        cout << "슈퍼맨이 숨을 쉽니다" << endl;
    }
};
void toBreath(Animal* a){
    a->breath();
}
void toFly(){

}
int main() {
    SetConsoleOutputCP(65001);

        // 객체화되지 않느다.
    // Animal* a = new Animal();
    // a->breath();

    Dog* d = new Dog();
    Bird* b = new Bird();
    Human* h = new Human();
    Superman* s = new Superman();
    toBreath(d);

    return 0;
}