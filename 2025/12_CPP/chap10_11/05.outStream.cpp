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
    friend ostream& operator<<(ostream& os, Point & p);
}; 

ostream& operator<<(ostream& os, Point & p){
    os << "x = "<< p.x <<", y = "<<p.y << endl;
    return os;
}

int main() {
    SetConsoleOutputCP(65001);
    
    //cout.operator<<("hello cpp").operator<<(3);

    //cout << "hello cpp" << 3;
    Point p(10,5);
    p.print();
    //cout operator<<(p);
    cout << p;
    return 0;
}