#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
class Point{
private:
    int x, y;
public:
    Point(int x, int y):x(x),y(y){};
    // 맴버함수의 전치단항연산자 재정의
    Point& operator++(){
        this->x++;
        this->y++;
        return *this;
    }
    friend Point& operator--(Point& p);    
    virtual void print()const{
        cout << this->x <<","<<this->y<< endl;
    }
};
// 전치단항연산자 전역함수
Point& operator--(Point& p){
    p.x--;
    p.y--;
    return p;
}

int main() {
    SetConsoleOutputCP(65001);
    Point p1(10,5);
    ++p1;
    --p1;
    p1.print();
    return 0;
}