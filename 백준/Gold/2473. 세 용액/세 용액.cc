#include <iostream>
#include <algorithm>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr[5000] = { 0, };
int main(void) {
	FAST_IO;
	
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	sort(arr, arr + n);
	long long result = 0x7fffffffffffffff;
	int result_arr[3];
	for (int i = 0; i < n; i++) {
		int st = i + 1, en = n - 1;
		while (st < en) {
			long long value = arr[st] + arr[en];
			if (llabs(value+arr[i]) < result) {
				result = llabs(value+arr[i]);
				result_arr[0] = arr[i];
				result_arr[1] = arr[st];
				result_arr[2] = arr[en];
			}
			long long sum = value + arr[i];
			if (sum >0) {
				en--;
			}
			else if (sum <0) {
				st++;
			}
			else if (sum ==0) {
				break;
			}

		}
	}
	sort(result_arr, result_arr + 3);
	for (int i = 0; i < 3; i++) {
		cout << result_arr[i] << " ";
	}
	return 0;
}