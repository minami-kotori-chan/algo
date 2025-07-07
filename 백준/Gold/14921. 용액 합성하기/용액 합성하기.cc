#include <iostream>
#include <algorithm>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr[1000000] = { 0, };
int main(void) {
	FAST_IO;
	
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	int st = 0;
	int en = n-1;
	int result=0x7fffffff;
	while (st < en) {
		int v = arr[st]+arr[en];
		if (abs(v) < abs(result)) {
			result = v;
		}
		if (v > 0) {
			en--;
		}
		else if (v < 0) {
			st++;
		}
		else {
			break;
		}
	}
	cout << result;
	return 0;
}