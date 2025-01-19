#include <iostream>
#include <algorithm>
using namespace std;
int main(void) {
	int a, b,c,d;
	int maximum=0;
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	cin >> a>>b;
	c = min(a, b);
	d = max(a, b);
	for (int i = 1; i <=c; i++) {
		if (a%i == 0 && b % i == 0) {
			maximum = i;
		}
	}
	cout << maximum << "\n";
	int i = 1;
	while (i * c % d != 0) {
		i++;
	}
	cout << c * i << "\n";
}