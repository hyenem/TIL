#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

class TmpObject{
private :
    int num = 10;
public :
    TmpObject(){
        cout << "TmpObject 생성자" << endl;
    }
    TmpObject(int num): num(num){
        cout << "TmpObject(int) 생성자" << endl;
    }
    ~TmpObject(){
        cout << "TmpObject 소멸자" << endl;
    }
    void print(){
        cout << "print num = " << num << endl;
    }
    void print()const{
        cout << "print const num = " << num << endl;
    }
};
int main() {
    SetConsoleOutputCP(65001);

    TmpObject();
    cout << "--------------------" << endl;
    TmpObject(100).print();
    cout << "--------------------" << endl;
    const TmpObject& ref = TmpObject(200);
    ref.print();
    cout << "--------------------" << endl;
    
    return 0;
}