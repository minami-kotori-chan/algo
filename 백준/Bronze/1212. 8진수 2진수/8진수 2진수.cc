#include <iostream>
using namespace std;


int main(void) {
	int n,m,s;
	int outset[3];
	int valid_check = 0;
	string str;
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	cin >> str;
	if (str.size() == 1 && str[0] == '0') {
		cout << '0';
	}
	else {
		for (const auto& s : str) {
			int v = s - '0';
			outset[0] = v / 4;
			outset[1] = (v % 4) / 2;
			outset[2] = (v % 4) % 2;
			for (int i = 0; i < 3; i++) {
				if (outset[i] == 0 && !valid_check) {
					continue;
				}
				else {
					valid_check = 1;
					cout << outset[i];
				}
			}
		}
	}
	


	return 0;
}