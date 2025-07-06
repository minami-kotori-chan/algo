#include <iostream>
#include <algorithm>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr[100000] = { 0, };
int main(void) {
	FAST_IO;
	
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	int st = 0, en = n-1;
	int result = 0x7fffffff;
	int result1, result2;
	while (st<en) {
		int v = arr[st] + arr[en];
		if (result > abs(v)) {
			result1 = arr[st];
			result2 = arr[en];
			result = abs(v);
		}
		if (v < 0) {
			st += 1;
		}
		else if (v > 0) {
			en -= 1;
		}
		else {
			break;
		}
	}
	cout << result1<<" "<<result2;
	return 0;
}