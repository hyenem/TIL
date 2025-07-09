#include <iostream>


//static(c++) : 위치 : 전역변수 : 선언된.c 파일안에서만 사용가능하다
//지역변수 : 함수가 끝나도 변수가 사라지지안는다
//맴버변수 : 객체의변수가 아니라 클래스의 변수가 된다
//1. 객체를 선언하지 안고 변수의 사용이 가능하다
//2. 모든 객체의 전역변수 역활을 하기된다
//
//맴버함수 : 객체를 선언하지 안고 함수의 사용이 가능하다

using namespace std;

class SoSimple
{
private:
	
public:
	static int simObjCnt;
	SoSimple()
	{
		simObjCnt++;
		cout << simObjCnt << "번째 SoSimple 객체" << endl;
	}
};
int SoSimple::simObjCnt = 0;

class SoComplex
{
private:
	static int cmxObjCnt;
public:
	SoComplex()
	{
		cmxObjCnt++;
		cout << cmxObjCnt << "번째 SoComplex 객체" << endl;
	}
	SoComplex(SoComplex& copy)
	{
		cmxObjCnt++;
		cout << cmxObjCnt << "번째 SoComplex 객체" << endl;
	}
};

int SoComplex::cmxObjCnt = 0;

int main(void)
{
	// SoSimple sim1;
	// SoSimple sim2;
	// 정적선언방식
	SoComplex cmx1;
	// 복사생성자를 이용하여 객체를 만들때
	SoComplex cmx2 = cmx1;
	// 임시객체를 이용할때 
	SoComplex();
	// static 을 외부에서 접근하려면 public 으로 선언하여야 한다
	// 클래스명::스태틱변수 형태로 사용하셔야 합니다
	// cout << SoSimple::simObjCnt << endl;
	return 0;
}