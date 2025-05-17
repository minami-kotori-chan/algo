#include <iostream>
#include <string>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int main(void) {
	FAST_IO;
	int t;
	cin >> t;
	for (int cnt = 0; cnt < t; cnt++) {
		int arr[10] = { 0, };
		int result = 0;
		int n;
		cin >> n;
		if (n == 0) {
			cout << "Case #"<<cnt+1<<": INSOMNIA"<<"\n";
			continue;
		}
		int v=1;
		while (result < 10) {
			int k = n*v;
			while (k > 0) {
				if (arr[k % 10] == 0) { arr[k % 10] = 1; result++; };
				k /= 10;
			}
			if (result == 10) {
				break;
			}
			else {
				v++;
			}
		}
		cout << "Case #" << cnt + 1 << ": "<<n*v<<"\n";
	}
	
	return 0;
}