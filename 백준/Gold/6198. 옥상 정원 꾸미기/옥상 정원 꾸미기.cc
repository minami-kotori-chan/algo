#include <iostream>
#include <deque>
using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int main(void) {
	FAST_IO;
	deque<int> que;
	int n;
	unsigned int result=0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		while (!que.empty() && que.back()<=temp) {
			que.pop_back();
		}
		result += que.size();
		que.push_back(temp);
	}
	cout << result;
	return 0;
}