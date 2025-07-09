#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
class Point{
private:
    int x, y;
public:
    Point(int x, int y):x(x),y(y){};
    
    virtual void print()const{
        cout << this->x <<","<<this->y<< endl;
    }

    Point& operator+(int a){
        this->x += a;
        this->y += a;
        return *this;
    }
    friend Point& operator+(int a, Point& p);
    friend Point& operator+(Point&p1 , Point& p2);
}; 
Point& operator+(int a, Point& p){
    p.x += a;
    p.y += a;
    return p;
};
Point& operator+(Point&p1 , Point& p2){
    p1.x += p2.x;
    p1.y += p2.y;
    return p1;
};

int main() {
    SetConsoleOutputCP(65001);
    Point p(10,5);
    p.print();

    //3.operator+(p)//p.operator+(3).operator+(2);
    3 + p +3 + 2 + p + 2;
    p.print();

    return 0;
}