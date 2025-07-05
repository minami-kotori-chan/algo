#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr1[500000] = { 0, };
int arr2[500000] = { 0, };

int main(void) {
	FAST_IO;
	
	int n, k;
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> arr1[i];
	}
	for (int i = 0; i < k; i++) {
		cin >> arr2[i];
	}
	sort(arr1, arr1 + n);
	sort(arr2, arr2 + k);
	vector<int> vc;
	for (int i = 0; i < n; i++) {
		if (binary_search(arr2, arr2 + k, arr1[i])) {
			continue;
		}
		else {
			vc.push_back(arr1[i]);
		}
	}
	cout << vc.size()<<"\n";
	for (const auto& i : vc) {
		cout << i << " ";
	}
	return 0;
}