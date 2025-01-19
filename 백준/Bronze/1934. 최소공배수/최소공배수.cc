#include <iostream>
#include <algorithm>
using namespace std;
int main(void) {
	int a, b,c,d,n;
	int maximum=0;
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		c = min(a, b);
		d = max(a, b);

		int j = 1;
		while ((j * c) % d != 0) {
			j++;
		}
		cout << c * j << "\n";
	}
}