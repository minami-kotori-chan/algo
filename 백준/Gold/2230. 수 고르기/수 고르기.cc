#include <iostream>
#include <algorithm>
using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr[100000];

int main(void) {
	FAST_IO;
	
	int n, m;
	cin >> n >> m;
	
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	
	int p1 = 0, p2 = 0;
	int result = 0x7fffffff;
	sort(arr, arr + n);

	while (p1 < n && p2 < n) {
		if (arr[p2]-arr[p1] >= m) {
			result = min(result, arr[p2]-arr[p1]);
			p1++;
		}
		else {
			p2++;
		}
	}
	cout << result;
	return 0;
}