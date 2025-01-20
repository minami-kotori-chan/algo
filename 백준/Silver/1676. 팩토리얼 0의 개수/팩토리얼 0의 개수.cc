#include <iostream>

using namespace std;

int fact_zero(const int& n) {
	int count = 0;
	for (int i = 2; i <= n; i++) {
		if ( i % 5 == 0) {
			int v = i;
			while (v%5==0) {
				count++;
				v /= 5;
			}
		}
	}
	return count;
}

int main(void) {
	int n;
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	cin >> n;
	cout<<fact_zero(n);
	
	return 0;
}