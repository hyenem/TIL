#include <iostream>
#include <cstring>
using namespace std;

int main() {
	string s1 = "Hello";
	string s2 = "Hello scsa";
	string s3 = s1 + s2;

	cout << s3 << endl;

	s3 += s2;
	if (s3 == s2) {

	}

	return 0;
}