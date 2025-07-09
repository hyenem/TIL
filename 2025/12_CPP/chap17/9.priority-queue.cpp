#include <iostream>
#include <queue>
#include <string>
#include "Person.h"
/*
	priority-queue
	정렬기준대로 정렬(heap 정렬)
	push, top, pop : 최대값이 리턴된다

*/
struct compare {
	bool operator()(int a, int b) {
		return a >  b;
	}
};
int main() {
	priority_queue<int> pq;
	for (const int n : {1, 8, 5, 6, 3, 4, 0, 9, 7, 2}) {
		pq.push(n);
	}
	for (int i = 0; i < 10; i++) {
		cout << pq.top() << " ";
		pq.pop();
	}
	cout << endl << endl;

	priority_queue<int, vector<int>, compare> pq1;
	for (const int n : {1, 8, 5, 6, 3, 4, 0, 9, 7, 2}) {
		pq1.push(n);
	}
	for (int i = 0; i < 10; i++) {
		cout << pq1.top() << " ";
		pq1.pop();
	}
	cout << endl;




	/*q.push(new Person("둘리", 7));
	q.push(new Person("도우너", 8));
	q.push(new Person("또치", 9));

	q.front()->printPerson();
	q.pop();
	q.front()->printPerson();
	q.back()->printPerson();*/
	return 0;
}
