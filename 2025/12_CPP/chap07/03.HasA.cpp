#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

class Gun{
public :
    void shot(){
        cout << "총을 쏩니다" << endl;
    }
};
class Police{
private :
    Gun g;
public :
    void carefullShot(){
        cout << "경찰관이 조심스럽게 ";
        g.shot();
    }
};
int main() {
    SetConsoleOutputCP(65001);

    Police p;
    p.carefullShot();

    return 0;
}