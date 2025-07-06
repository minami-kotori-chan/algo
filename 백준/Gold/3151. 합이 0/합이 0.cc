#include <iostream>
#include <algorithm>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr[10000] = { 0, };
int main(void) {
	FAST_IO;
	
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	sort(arr, arr + n);
	long long result = 0;
	for (int i = 0; i < n - 1; i++) {
		for (int j = i + 1; j < n; j++) {
			int st= lower_bound(arr, arr + n, -1 * (arr[i]+arr[j]))-arr;
			int en = upper_bound(arr, arr + n, -1 * (arr[i] + arr[j])) - arr;
			if (en > max(st, j + 1)) {
				result += (en - max(st, j + 1));
			}
		}
	}
	cout << result;
	return 0;
}