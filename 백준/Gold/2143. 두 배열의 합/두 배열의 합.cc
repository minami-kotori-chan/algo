#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr1[1000] = { 0, };
int arr2[1000] = { 0, };
int main(void) {
	FAST_IO;
	
	int t, n,m;
	cin >> t >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr1[i];
	}
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> arr2[i];
	}
	vector<int> vc1;
	for (int i = 0; i < n; i++) {
		int sum = 0;
		for (int j = i; j < n; j++) {
			sum += arr1[j];
			vc1.push_back(sum);
		}
	}
	vector<int> vc2;
	for (int i = 0; i < m; i++) {
		int sum = 0;
		for (int j = i; j < m; j++) {
			sum += arr2[j];
			vc2.push_back(sum);
		}
	}
	long long result = 0;
	sort(vc1.begin(), vc1.end());
	sort(vc2.begin(), vc2.end());
	for (const auto& i : vc1) {
		int count = upper_bound(vc2.begin(), vc2.end(), t - i)- lower_bound(vc2.begin(), vc2.end(), t - i);
		result += count;
	}
	cout << result;
	return 0;
}