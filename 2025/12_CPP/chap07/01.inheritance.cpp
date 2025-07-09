/*
    상속
        정의 : sub calss 가 super class의 모든 것을 물려받는 것
        목적 : 확장, 재정의, 객체의 형변환 기반
*/
#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

class Father{
private :
protected :
    int num = 10;
public :
    int num2 = 10;
    Father(){cout << "Father 생성자" << endl;}
    Father(int num):num(num){cout << "Father(num) 생성자" << endl;}
    ~Father(){cout << "Father 소멸자" << endl;}
    void print(){cout <<"num = "<< num << endl;}
};
class Son : public Father{
private :
protected :
public :
    int num2=20;
    Son(){cout <<"Son 생성자"<< endl;}
    Son(int num):Father(num){}
    ~Son(){cout << "Son 소멸자" << endl;}
    void print(){
        cout << "son print num = " << num << endl;
    }
};
int main() {
    SetConsoleOutputCP(65001);

    // Father f;
    // f.print();

    // Son s(100);
    // s.num; //부모의 private은 접근 불가능
    // s.print();

    Father f;
    cout << f.num2 << endl;

    Son s;
    cout << s.num2 << endl;

    return 0;
}