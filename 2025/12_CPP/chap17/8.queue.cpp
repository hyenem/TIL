#include <iostream>
#include <queue>
#include <string>
#include "Person.h"
/*
	queue
	FIFO 의 자료구조
	front : 가장 앞에는 요소를 리턴
	back : 가장 뒤에는 요소를 리턴 
	pop : 가장앞에있는 요소를 리턴후 삭제
	push : 맴뒤에 삽입
*/
int main() {
	queue<Person*> q;
	q.push(new Person("둘리", 7));
	q.push(new Person("도우너", 8));
	q.push(new Person("또치", 9));

	q.front()->printPerson();
	q.pop();
	q.front()->printPerson();
	q.back()->printPerson();
	return 0;
}
