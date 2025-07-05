#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr[1000000] = { 0, };

int main(void) {
	FAST_IO;
	
	int n, k;
	cin >> n >> k;
	for (int i = 0; i < k; i++) {
		cin >> arr[i];
	}
	int st = 1, en = 0x3fffffff;
	int result = 0;
	while (st <= en) {
		int mid = (st + en) / 2;
		int cnt = 0;
		for (int i = 0; i < k; i++) {
			cnt += arr[i] / mid;
		}
		if (cnt >= n) {
			st = mid + 1;
			result = max(result, mid);
		}
		else {
			en = mid - 1;
		}
	}
	cout << result;
	return 0;
}