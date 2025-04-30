#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int main(void) {
	FAST_IO;
	unordered_set<int> map;
	vector<int> vc;
	int n;
	int result=0;
	cin >> n;
	for (int i = 0; i < n; i++){
		int temp;
		cin >> temp;
		vc.push_back(temp);
	}

	for (int i = 0; i < n; i++) {
		for (int j = i; j < n; j++) {
			map.insert(vc[i] + vc[j]);
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = i; j < n; j++) {
			int temp = abs(vc[i] - vc[j]);
			if (map.count(temp)) result = max(result, max(vc[i],vc[j]));
		}
	}

	cout << result;
	return 0;
}