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
public:
    
    Point(int a, int b):x(a),y(b){}
    // 맴버함수 연산자 오버로드
    // Point& operator+(int a){
    //     this->x += a;
    //     this->y += a;
    //     return *this;
    // }
    // 맴버함수 연산자 오버로드
    // Point& operator+(Point& p){
    //     this->x += p.x;
    //     this->y += p.y;
    //     return *this;
    // }
    friend Point& operator+(Point& p , int a);
    friend Point& operator+(Point& p1 , Point& p2);
    friend Point& operator+(int a , Point& p);        
    virtual void print()const{
        cout << this->x <<","<<this->y<< endl;
    }
};
// 전역함수 연산자 오버로드
Point& operator+(Point& p , int a){
    p.x += a;
    p.y += a;
    return p;
}
Point& operator+(Point& p1 , Point& p2){
    p1.x += p2.x;
    p1.y += p2.y;
    return p1;
}
Point& operator+(int a , Point& p){
    p.x += a;
    p.y += a;
    return p;
}

int main() {
    SetConsoleOutputCP(65001);
    int a=10, b=5;
    cout << add(a,b) << endl;
    cout << a + b << endl;
    Point p1(10,5);
    Point p2(15,10);
    // Point res = p1.operator+(a);   
    Point res = p1 + a;
    res.print();
    Point res2 = p1 + p2;
    res2.print();
    // 맴버함수 구현은 객체타입이 먼저 나오는 연산자만 가능하다
    // 전역함수로 구현하시면 객체타입이 먼저 나오지 않아도 된다
    // 그러나 전역함수로 연산자오버로드를 하게되면 public 이 아닌 맴버에 대해 접근 권한을 가질수 없다
    Point res3 =  3 + p1;
    // 또 그러나 friend 를 사용해서 private 맴버에 접근권한을 취할수 있다

    return 0;
}