#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
class Point{
private :
    int x, y;
public :
    friend ostream& operator<<(ostream& cout, Point& p);

    Point(){
        cout << "기본생성자" << endl;
    }
    Point(int x, int y):x(x), y(y){}
    //복사생성자
    Point(const Point& copy): x(copy.x), y(copy.y){
        cout << "복사생성자" << endl;
    }
    virtual void print()const{
        cout << this->x << ", " << this->y <<endl;
    }
    // 기본 대입 연산자
    Point& operator=(const Point& copy){
        cout << "기본 대입 연산자" << endl;
        this->x = copy.x;
        this->y = copy.y;
        return *this;
    }
};
ostream& operator<<(ostream& cout, Point& p){
    cout << "x= " << p.x << ", y= " << p.y << endl;
    return cout;
}
int main() {
    SetConsoleOutputCP(65001);

    Point s(10, 5);

    // 복사생성자 호출
    Point s1 = s;
    Point s2;

    s2 = s1;

    cout << s << ", " << s1 << endl;
    cout << s2 << endl;

    return 0;
}