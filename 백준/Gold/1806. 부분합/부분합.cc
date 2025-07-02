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
	long long sum = arr[0];
	int p1 = 0;
	int p2 = 0;
	int result = 100001;

	while (p1 < n) {
		if (sum >= m) {
			result = min(result, p2 - p1 + 1);
			if (p1 < p2) {
				sum -= arr[p1];
				p1++;
				continue;
			}
			else break;
		}
		p2++;
		if (p2 >= n) break;
		sum += arr[p2];
		
	}
	if (result == 100001) {
		cout << 0;
	}
	else {
		cout << result;
	}
	return 0;
}