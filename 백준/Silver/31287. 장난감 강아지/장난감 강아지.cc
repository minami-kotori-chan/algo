#include <iostream>
#include <string>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int main(void) {
	FAST_IO;
	int n, k;
	string str;
	cin >> n >> k;
	cin >> str;
	int row = 0, col = 0;
	int result = 0;
	for (int count = 0; count < k && count < n; count++) {
		for (const char& i : str) {
			if (i == 'U') row++;
			else if (i == 'D') row--;
			else if (i == 'R')col++;
			else col--;
			if (row == 0 && col == 0)
			{
				result = 1;
				break;
			}

		}
	}

	if (result) {
		cout << "YES";
	}
	else {
		cout << "NO";
	}
	return 0;
}