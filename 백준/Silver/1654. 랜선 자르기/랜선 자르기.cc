#include <iostream>
#include <algorithm>
using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr[10000] = { 0, };

int main(void) {
	FAST_IO;
	
	int n,k;
	cin >> k>>n;
	for (int i = 0; i < k; i++) {
		cin >> arr[i];
	}
	long long st = 0, en = 0x7fffffff;
	long long result = -1;
	while (st <= en) {
		long long mid = (st + en) / 2;
		long long cnt = 0;
		for (int i = 0; i < k; i++) {
			cnt += arr[i] / mid;
		}
		if (cnt >= n) {
			st = mid+1;
			result = max(result, mid);
		}
		else {
			en = mid-1;
		}
	}
	cout << result;
	return 0;
}