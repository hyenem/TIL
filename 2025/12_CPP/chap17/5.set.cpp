#include <iostream>
#include <set>
#include <algorithm>
#include "Person.h"
using namespace std;
/*
	set 
		원소가 중복되지 안는다
		정렬이 된다
		insert 함수로 삽입된다
		중복을 허용하지 안는다
		그래서 추가되는 중복데이타를 무시된다
*/

template <typename T>
void print(set<T>&s) {
	for (Person* p : s){
		p->printPerson();
	}
	cout << endl << endl;
}


int main() {
	set<Person*> sets;
	Person* p1 = new Person("둘리", 7);
	Person* p2 = new Person("도우너", 8);
	Person* p3 = new Person("도치", 9);
	
	sets.insert(p1);
	sets.insert(p2);
	sets.insert(p3);

	print(sets);
	// 중복은 무시된다
	sets.insert(p2);
	print(sets);

	// 찾기 (둘리)
	// set<Person*>::iterator itr = sets.find(p1);
	// (*itr)->printPerson();
	// 찾기 (도우너)
	auto itr = sets.find(p2);
	(*itr)->printPerson();
	
	return 0;
}
