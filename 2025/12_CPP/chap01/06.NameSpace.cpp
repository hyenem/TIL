#include <iostream>
#include <cstdlib>
#include <windows.h>

namespace AA{
    int a = 10;
    void print(int a){
        cout << "namespace AA " << a << endl;
    }
}
namespace BB{
    int a = 20;
    void print(int a){
        cout << "namespace BB " << a << endl;
    }
}
namespace CC{
    void print(){};
    namespace DD{
        void print(){};
    }
}

using AA::print;
using std::cout;
using std::endl;

using namespace std;

int main() {
    SetConsoleOutputCP(65001);

    cout << AA::a << ", " << BB::a << endl;
    cin >> AA::a;

    AA::print(3);
    BB::print(10);
    CC::print();
    CC::DD::print();

    print(3);
    BB::print(3);

    return 0;
}