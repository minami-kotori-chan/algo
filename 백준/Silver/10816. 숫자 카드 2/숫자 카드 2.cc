#include <iostream>
#include <algorithm>
using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr[500000];

int main(void) {
	FAST_IO;
	
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	sort(arr, arr + n);
	int m;
	cin >> m;
	for (int i = 0; i < m; i++) {
		int temp;
		cin >> temp;
		cout<<upper_bound(arr, arr + n, temp) - lower_bound(arr, arr + n, temp)<<" ";
		
	}
	
	return 0;
}