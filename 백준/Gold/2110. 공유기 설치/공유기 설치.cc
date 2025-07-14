#include <iostream>
#include <algorithm>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr[200000] = { 0, };
int main(void) {
	FAST_IO;
	
	int n, c;
	cin >> n >> c;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	sort(arr, arr + n);
	int st = 1, en = arr[n - 1]-arr[0];
	int result = 0x7fffffff;

	while (st <= en) {
		int mid = (st + en) / 2;
		int prev = arr[0];
		int count = 1;
		for (int i = 1; i < n; i++) {
			if (arr[i]-prev>=mid) {
				count++;
				prev = arr[i];
			}
		}
		if (count >= c) {
			result = mid;
			st = mid+1;
		}
		else {
			en = mid-1;
		}
	}
	cout << result;
	return 0;
}