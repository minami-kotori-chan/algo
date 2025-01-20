#include <iostream>
#include <vector>
#include <deque>
using namespace std;


int main(void) {
	int n,m,s;
	string str;
	deque<char> dq;
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	cin >> str;
	for (auto& i : str) {
		dq.push_back(i);
	}

	if (str.size() % 3 > 0) {
		for (int i = 0; i < 3 - (str.size() % 3); i++) {
			dq.push_front('0');
		}
	}
	while (dq.size() > 0) {
		int first = dq.front() - '0';
		dq.pop_front();
		int two = dq.front() - '0';
		dq.pop_front();
		int three = dq.front() - '0';
		dq.pop_front();

		cout << (first * 4 + two * 2 + three);
	}
	return 0;
}