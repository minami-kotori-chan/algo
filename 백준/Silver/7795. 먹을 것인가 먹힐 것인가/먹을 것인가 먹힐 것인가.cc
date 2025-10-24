#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int main(void) {
	FAST_IO;
	int t;
	cin >> t;
	while (t--) {
		int n, m;
		cin >> n >> m;
		vector<int> a(n);
		vector<int> b(m);
		for (int i = 0; i < n; i++) {
			cin >> a[i];
		}
		for (int i = 0; i < m; i++) {
			cin >> b[i];
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		int sum = 0;
		for (const auto& i : a) {
			sum+=upper_bound(b.begin(), b.end(),i-1)-b.begin();
		}
		cout << sum << "\n";
		a.clear();
		b.clear();
	}
	return 0;
}