#include <iostream>
#include <string>
#include <deque>
#include <algorithm>

using namespace std;
/*
	deque
		동적배열
		시작과 끝에서 삽입과 삭제를 수행하는 벡터
		push_front, push_back
		벡터와 같이 물리적으로 연속적이지는 안다
*/
template <typename T>
void print(deque<T> deq) {
	for (typename deque<T>::iterator itr = deq.begin(); itr != deq.end(); itr++) {
		cout << (*itr) << " ";
	}
	cout << endl << endl;
}

int main() {
	deque<int> deq;
	deq.push_back(1);
	deq.push_back(3);
	deq.push_back(5);
	deq.push_back(7);
	deq.push_back(9);
	print(deq);
	// 앞에거 제거
	deq.pop_front();
	print(deq);
	// 뒤에거 제거
	deq.pop_back();
	print(deq);
	return 0;
}