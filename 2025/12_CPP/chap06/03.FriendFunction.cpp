#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

class Point;
class PointOperator{
public :
    Point pointAdd(const Point& p1, const Point& p2);
};
class Point{
private :
    int x, y;
public :
    Point(const int& x, const int& y):x(x), y(y){}
    friend Point PointOperator::pointAdd(const Point& p1, const Point& p2);
    // void print(){
    //     cout << x << ", " << y << endl;
    // }
    friend void print(const Point& p);
};
Point PointOperator::pointAdd(const Point& p1, const Point& p2){
    Point p(p1.x+p2.x, p1.y+p2.y);
    return p;
}

void print(const Point& p){
    cout << p.x << ", " << p.y << endl;
}

int main() {
    SetConsoleOutputCP(65001);

    Point p1(1, 3), p2(5, 9);
    PointOperator op;
    Point res = op.pointAdd(p1, p2);
    print(res);

    return 0;
}