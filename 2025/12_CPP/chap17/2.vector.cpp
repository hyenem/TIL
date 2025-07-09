#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
/*
	vector 
		동적배열구조 (크기가 자동조정)'
		push_back, end, begin, back, front, size .....
		push_back을 많이 씀니다
		vector push_front 없어요
*/
class Person {
private:
public:
	string name;
	int age;
public:
	Person(string name, int age) :name(name), age(age) {}
	void print() {
		cout << name << "," << age << endl;
	}
};

int main(){
	vector<Person*> persons;
	persons.push_back(new Person("둘리", 7));
	persons.push_back(new Person("도우너", 8));
	persons.push_back(new Person("또치", 9));
	
	/*for (vector<int>::size_type i = 0; i < persons.size(); i++)
	{
		persons[i]->print();
	}*/

	//cout << endl;
	for (vector<Person*>::iterator itr = persons.begin() ; itr != persons.end() ; itr++)
	{
		(*itr)->print();
	}

	// for_each
	for_each(persons.begin(), persons.end(), /* 함수*/ [](Person* p) { p->print(); });

	// 삭제
	vector<Person*>::iterator itr = persons.begin();
	for (; itr != persons.end(); itr++)
	{
		if ((*itr)->name == "둘리") {
			persons.erase(itr);
			itr = persons.begin();
		}
		// 크기가 변경되었기 때문에 다시 초기화 한다
		(*itr)->print();
	}


	vector<int> vec;
	vec.push_back(1);
	vec.push_back(3);
	vec.push_back(5);
	vec.push_back(7);

	for (vector<int>::size_type i = 0; i < vec.size(); i++)
	{
		cout << vec[i] << " ";
	}
	cout << endl;
	return 0;
}