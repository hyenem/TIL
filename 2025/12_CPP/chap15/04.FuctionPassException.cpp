#include <iostream>
#include <cstdlib>
#include <windows.h>
using namespace std;
int devide(int n1, int n2){

    if(n2==0) throw n2;

    cout << "몫 : " << n1/n2 << endl;
    cout << "나머지 : " << n1%n2 << endl;

    return 0;

}
int main() {
    SetConsoleOutputCP(65001);

    int n1, n2;
    cout << "두 수를 입력하세요 : " << endl;
    cin >> n1 >> n2;

    try{
        devide(n1, n2);
        cout << "몫과 나머지가 출력되었습니다." << endl;
    } catch(int ex){
        cout << "제수는 " << ex <<"이 될 수 없습니다. 다시 실행하세요." << endl;
    }

    return 0;
}