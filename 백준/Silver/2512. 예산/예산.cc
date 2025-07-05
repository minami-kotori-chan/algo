#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr[10000] = { 0, };

int main(void) {
	FAST_IO;
	
	int n, m;
	cin >> n;
	int arr_max = 0;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		arr_max = max(arr_max, arr[i]);
	}
	cin >> m;
	int st = 0, en = m;
	int result = 0;
	while (st <= en) {
		int mid = (st + en) / 2;
		int sum = 0;
		for (int i = 0; i < n; i++) {
			if (arr[i] <= mid) {
				sum += arr[i];
			}
			else {
				sum += mid;
			}
		}

		if (sum > m) {
			en = mid - 1;
		}
		else {
			st = mid + 1;
			result = max(result, mid);
		}
	}
	if (result > arr_max) {
		cout << arr_max;
	}
	else {
		cout << result;
	}
	
	return 0;
}