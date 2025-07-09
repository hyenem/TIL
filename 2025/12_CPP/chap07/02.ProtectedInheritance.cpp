#include <iostream>

using namespace std;

class Father {
private:
	int num1 = 10;
protected:
	int num2 = 20;
public:
	int num3 = 30;
	
};
// class Son : public Father {
// public:
// 	Son() {

// 	}
// };
class Son : protected Father {
public:
	Son() {

	}
};
//class Son : private Father {};

int main() {
	Son s;
	//s.num3

	return 0;
}