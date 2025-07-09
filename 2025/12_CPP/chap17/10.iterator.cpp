#include <iostream>
#include <vector>

using namespace std;
/*
	iterator 반복자
	컨테이너에 있는 원소를 순차적으로 접근할수 있게 합니다
	모든 컨터이너가 같은 방법을 사용합니다
	::iterator
	::const_iterator
	컨테이너마다 사용되는 iterator는 다르다
	그래서 vertor , dequeue 에 사용되는 반복자는 산술연산이 된다
*/
int main() {
	vector<int> v;
	for (int i = 0; i < 10; i++)
		v.push_back(i);
	vector<int>::iterator itr;
	itr = v.begin();
	cout << "------while----------" << endl;
	while (itr != v.end()) {
		cout << *itr << " ";
		++itr;
	}
	cout << endl;
	cout << "------for-------------" << endl;
	for (auto itr = v.begin(); itr != v.end(); ++itr) {
		cout << *itr << " ";
	}
	cout << endl;
	cout << "------for-each---------" << endl;
	for (auto& itr : v) {
		cout << itr << " ";
	}


	return 0;
}