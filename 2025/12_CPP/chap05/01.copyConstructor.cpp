#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
/*
    복사 생성자
    1) 객체를 이용하여 객체를 선언할 때
    2) 함수의 인자로 객체를 넘길 때
    3) 함수의 리턴으로 객체를 넘길 때

    복사 생성자가 호출되지 않는 경우
    위의 3가지 경우에서 참조변수를 통해 인자나 리턴을 넘겨주게 되면 복사생성자는 호출되지 않음
    객체가 생성되는 것이 아니고 이름만 새로 만들어 지는 것이니까
*/
class Simple{
private :
    int num1, num2;
    // 깊은 복사 코드가 필요하기 때문에 복사생성자에서도 작업을 해주어야 한다.
    char* name;
public :
    Simple(){
        cout << "기본 생성자" << endl;
    }
    Simple(int n1, int n2, const char* name):num1(n1), num2(n2){
        cout << "num1, num2 생성자" << endl;
        this->name = new char[strlen(name)+1];
        strcpy(this->name, name);
    }
    Simple(const Simple& copy):num1(copy.num1), num2(copy.num2){
        cout << "복사 생성자" << endl;
        this->name = new char[strlen(name)+1];
        strcpy(this->name, name);
    }
    ~Simple(){
        delete[] name;
    }
    void print(){
        cout << num1 << ", "<<num2<<", "<< name << endl;
    }
    Simple& print(Simple& s){
        cout << num1 << ", "<<num2<<", "<< name << endl;
        return *this;
    }
};
void print(Simple s){

}
int main() {
    SetConsoleOutputCP(65001);

    Simple s1(10, 5, "이름");
    s1.print();
    Simple s2 = s1;
    // Simple s2(s1);
    s2.print();
    cout << &s1 << " " << &s2 << endl;

    print(s1);

    return 0;
}