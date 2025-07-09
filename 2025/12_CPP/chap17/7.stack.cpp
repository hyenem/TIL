#include <iostream>
#include <stack>
#include <string>
#include "Person.h"
/*
	stack
	FILO 의 자료구조
	push, pop, top 

*/
int main() {
	stack<Person*> s;
	s.push(new Person("둘리", 7));
	s.push(new Person("도우너", 8));
	s.push(new Person("또치", 9));

	s.top()->printPerson() ;
	s.pop();
	s.top()->printPerson();
	return 0;
}
