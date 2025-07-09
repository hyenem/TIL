#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;

class Girl;
class Boy{
private :
    int height;
    friend class Girl;
public:
    Boy(int height);
};
class Girl{
private :
    int tel;
public :
    Girl(int tel);
    void myBoyFriend(Boy& boy);
};
Boy::Boy(int height):height(height){
    
}
Girl::Girl(int tel):tel(tel){}
void Girl::myBoyFriend(Boy& boy){
    cout << boy.height << endl;
}

int main() {
    SetConsoleOutputCP(65001);

    Boy b(168);
    Girl g(12345678);
    g.myBoyFriend(b);

    return 0;
}