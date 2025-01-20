#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int uclead(const int& n,const int& m) {
	int big=max(n,m), small=min(n,m);
	while (big%small != 0) {
		int temp = big;
		big = small;
		small = temp % small;
	}
	return small;
}

int main(void) {
	int n,m,s;
	vector<int> vc;
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	cin >> n >> s;

	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		vc.push_back(abs(temp-s));
	}
	if (vc.size() > 1) {
		int get_gcd = uclead(vc[0], vc[1]);
		for (int i = 0; i < vc.size() - 1; i++) {
			get_gcd = uclead(get_gcd, vc[i + 1]);
		}
		cout << get_gcd;
	}
	else {
		cout << vc[0];
	}
	


	return 0;
}