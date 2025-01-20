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
	int n,m;
	vector<int> vc;
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> m;
		vc.clear();
		long long  result=0;
		for (int j = 0; j < m; j++) {
			int temp;
			cin >> temp;
			vc.push_back(temp);
		}
		for (int j = 0; j < vc.size()-1; j++) {
			for (int k = j+1; k < vc.size(); k++) {
				result+= uclead(vc[j], vc[k]);
			}
		}
		if (result == 0)
			result = m;
		cout << result << "\n";

	}
	return 0;
}