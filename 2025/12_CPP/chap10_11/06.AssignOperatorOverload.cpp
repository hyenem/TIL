#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
/*
    디폴트 대입연산자 
        객체를 자동으로 만들어지고
        객체가 대입연산자를 사용하게 되면 실행이 되어진다
        
*/
class Point{
private:
    int x, y;
    //char* name;
public:
    Point(){
        cout << "기본생성자" <<endl;
    };
    Point(int x, int y):x(x),y(y){
        cout << "int, int 생성자" <<endl;
    };
    // 복사생성자
    Point(const Point& copy):x(copy.x),y(copy.y){
        cout << "복사생성자" << endl;
    };
    // 기본 대입연산자 
    Point& operator=(const Point& copy){
        cout << "기본 대입연산자" << endl;
        this->x = copy.x;
        this->y = copy.y;
        return *this;
    }
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
    Point s(10,5);
    // 복사생성자
    Point s1 = s;
    Point s2;
    // 기본대입연산자오버로드
    s2 = s1;
    
    cout << s2 << endl;
    return 0;
}