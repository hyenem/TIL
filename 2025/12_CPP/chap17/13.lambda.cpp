#include <iostream>
#include <vector>
#include <algorithm> // for_each
using namespace std;

/*
	lambda 표현식
	함수선언방식의 구현으로 익명함수형태를 보이고
	함수포인터 처럼 사용되어짐니다
	형식
	[]()-> returntype {} () 실행

	[]: 람다함수 밖에서 선언된 변수를 람다함수 내부에서 
	사용할수 있게 정의하는 부분
		ex
		[&] 외부에서 선언된 변수를 참조형식으로 사용한다
			[&a]
		[=] 외부에서 선언된 변수를 복사형식으로 사용한다
			[=a]
		[this] 객체내에서 객체맴버를 사용하고자 할때 사용한다
	(): 파라미터 선언부분
	-> 리턴타입정의 사용되어진다
		만약 void라면 생략가능하다
	{} : 함수의 구현부
	() : 함수의 호출부(함수실행)
*/
int main() {
	int a = 10, b = 5;
	int res = [&]()->int {return a++ + b; }();
	cout << res << endl;
	cout << a << endl;

	vector<int> v;
	v.push_back(1);
	v.push_back(2);
	v.push_back(3);
	v.push_back(13);
	v.push_back(14);
	auto func = [](int val) {cout << val << " "; };
	// -> void return 이므로 생략가능
	for_each(v.begin(),v.end(),func);
	
	return 0;
}