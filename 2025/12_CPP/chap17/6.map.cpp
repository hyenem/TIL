#include <iostream>
#include <map>
#include <algorithm>
#include "Person.h"
using namespace std;
/*
	map
		set과 같은 구조이나 <key, value> 형식으로 구성된다
		key 는 중복될수 없다 같은 키값이 들어오면 업데이트가 된다
		key와 value를 pair를 이용하여 사용하거나 [key]=value 형태로 사용한다	
*/
template <typename K, class V>
void print(map<K,V>& m) {
	for (const auto& p : m){
		cout << p.first << " : ";
		p.second->printPerson();
	}
	cout << endl << endl;
}

int main() {
	map<string, Person*> m;
	m["1"] = new Person("둘리", 7);
	m["2"] = new Person("도우너", 8);
	m["3"] = new Person("또치", 9);

	print(m);
	return 0;
}