#include <iostream>
#include <vector>

using namespace std;

int main(void) {
	int n;
	vector<char> str;
	int arr[32] = { 0 };
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	cin >> n;
	int l = n;
	if (n == 0) {
		cout << "0";
	}
	else {
		while (l != 0) {
			if (l % -2 == 0) {
				str.push_back('0');
				l /= -2;
			}
			else {
				str.push_back('1');
				l = (l - 1) / -2;
			}
		}
	}
	for (int i = str.size()-1; i >= 0; i--) {
		cout << str[i];
	}
	return 0;
}