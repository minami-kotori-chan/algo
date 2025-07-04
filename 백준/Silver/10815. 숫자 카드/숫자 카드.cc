#include <iostream>
#include <algorithm>
using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr[500001] = { 0, };

int main(void) {
	FAST_IO;
	
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	sort(arr, arr + n);
	int m;
	cin >> m;
	for (int i = 0; i < m; i++) {
		int temp;
		cin >> temp;
		int st = 0, en = n - 1;
		int result = 0;
		while (st <= en) {
			int mid = (st + en) / 2;
			if (arr[mid] == temp) {
				result = 1;
				break;
			}
			else if (arr[mid] < temp) {
				st = mid+1;
			}
			else if (arr[mid] > temp) {
				en = mid-1;
			}
		}
		if (result) {
			cout << "1 ";
		}
		else {
			cout << "0 ";
		}
	}
	
	return 0;
}