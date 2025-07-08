#include <iostream>
#include <algorithm>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr[2000] = { 0, };
int main(void) {
	FAST_IO;
	
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	int result = 0;
	sort(arr, arr + n);
	for (int i = 0; i < n; i++) {
		int st = 0;
		int en = n - 1;
		while (st < en) {
			if (st == i) {
				st++;
				continue;
			}
			if (en == i) {
				en--;
				continue;
			}
			int v = arr[st] + arr[en];
			if (v > arr[i]) {
				en--;
			}
			else if (v < arr[i]) {
				st++;
			}
			else if (v == arr[i]) {
				result++;
				break;
			}

		}

	}
	cout << result;
	return 0;
}