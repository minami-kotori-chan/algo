#include <iostream>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int main(void) {
	FAST_IO;
	int n;
	cin >> n;
	long long int result=0;
	int prev_val=0;
	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		if (prev_val != 0) {
			result += temp * 4 + 2;
			result -= min(prev_val, temp) * 2;
		}
		else {
			result += temp * 4 + 2;
		}
		prev_val = temp;
	}
	cout << result;
	return 0;
}