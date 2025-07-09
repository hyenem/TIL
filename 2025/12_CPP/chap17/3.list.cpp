#include <iostream>
#include <string>
#include <list>
#include <algorithm>

using namespace std;
/*
	리스트
		양방향 연결리스트 구조
		메모리상 연속적이지는 안다
		검색은 배열보다 약간 느릴수 있지만 삽입 제거 가 빠르다
*/
int main() {
	list<int> ls;
	ls.push_back(1);
	ls.push_back(3);
	ls.push_back(5);
	
	for (list<int>::iterator itr = ls.begin(); itr != ls.end(); itr++)
	{
		cout << *itr << " " ;
	}
	cout <<  endl;
	// find 함수 사용
	list<int>::iterator itr = find(ls.begin(), ls.end(), 3);
	
	cout << (*itr) << endl;
	cout << endl;
	
	return 0;
}