#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
	vector<int> v;
	for (int i = 1; i <= 10; i++)
		v.push_back(i);
	cout << "------- min_element --------" << endl;
	auto val = min_element(v.begin(), v.end());
	cout << *val << endl;
	
	cout << "------- max_element --------" << endl;
	val = max_element(v.begin(), v.end());
	cout << *val << endl;

	cout << "------- find --------" << endl;
	val = find(v.begin(), v.end(),3);
	cout << *val << endl;
	return 0;
}