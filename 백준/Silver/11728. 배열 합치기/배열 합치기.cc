#include <iostream>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr1[1000000];
int arr2[1000000];
int result[2000000];
int main(void) {
	FAST_IO;
	
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> arr1[i];
	}
	for (int i = 0; i < m; i++) {
		cin >> arr2[i];
	}
	int p1 = 0;
	int p2 = 0;
	int index = 0;
	while (p1 < n || p2 < m) {
		if ((p1<n && arr1[p1] < arr2[p2]) || p2>=m) {
			result[index] = arr1[p1];
			index++;
			p1++;
		}
		else {
			result[index] = arr2[p2];
			index++;
			p2++;
		}

	}
	for (int i = 0; i < n + m; i++) {
		cout << result[i] << " ";
	}
	return 0;
}