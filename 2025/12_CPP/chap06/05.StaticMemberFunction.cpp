#include <iostream>
using namespace std;

class SoSimple
{
public:

	static int simObjCnt;
	int cnt;
public:
	SoSimple()
	{
		simObjCnt++;
	}
	static void printStaticCnt() {
		cout << "static simObjCnt : " << simObjCnt << endl;
		// static function 에서는 static 변수와 static 함수만 사용할수 있다
		// cout << " cnt : " << cnt << endl;
	}
};
// static member 변수를 꼭 초기화를 해주어야 한다
int SoSimple::simObjCnt = 0;

int main(void)
{

	SoSimple sim1;


	sim1.printStaticCnt();
	SoSimple::printStaticCnt();
	return 0;
}