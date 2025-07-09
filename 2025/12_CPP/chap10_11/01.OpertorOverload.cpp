#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

int add(int a, int b){
    return a+b;
}
class Point{
private :
    int x, y;
public :
    friend Point& operator+(int a, Point& p);
    friend Point& operator+(Point& p, int a);
    friend Point& operator+(Point& p1, Point& p2);
    Point(int a, int b): x(a), y(b){}
    // Point& operator+(int a){
    //     this->x += a;
    //     this->y += a;
    //     return *this;
    // }
    // Point& operator+(Point& p){
    //     this->x += p.x;
    //     this->y += p.y;
    //     return *this;
    // }
    void print()const{
        cout << this->x << ", " << this->y << endl;
    }
};
Point& operator+(Point& p, int a){
    p.x += a;
    p.y += a;
    return p;
}
Point& operator+(int a, Point& p){
    p.x += a;
    p.y += a;
    return p;
}
Point& operator+(Point& p1, Point& p2){
    p1.x += p2.x;
    p2.x += p2.y;
    return p1;
}
int main() {
    SetConsoleOutputCP(65001);

    int a = 10, b = 5;
    cout << add(a, b) << endl;
    cout << a + b << endl;

    Point p1(10, 5);
    Point p2(15, 10);
    // Point res = p1.operator+(a);//p1+a;
    Point res = p1 + a;
    res.print();
    Point res2 = p1 + p2;
    res2.print();
    // 멤버함수 구현은 객체 타입이 먼저 나오는 연산자마 ㄴ가능하다
    // 그러나 전역함수로 연산자 오버로드를 하게 되면 public이 아닌 맴버에 대해 접근 권한을 가질 수 없다.
    // Point res3 = 3.operator+(p1);
    Point res3 = 3+p1;

    return 0;
}