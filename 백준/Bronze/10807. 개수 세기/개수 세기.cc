#include <iostream>

using namespace std;

int main(void) {
	int n, v, count=0;
	int arr[100];

	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	cin>> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	cin >> v;

	for (int i = 0; i < n; i++)
		if (arr[i] == v)
			count++;
	cout << count << "\n";
	
}