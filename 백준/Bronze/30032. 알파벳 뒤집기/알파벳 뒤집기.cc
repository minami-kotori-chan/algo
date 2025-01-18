#include <iostream>
#include <vector>
using namespace std;
int main(void) {
	int n, d;
	string str[10];
	
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	cin >> n>> d;

	for (int i = 0; i < n; i++) {
		cin >> str[i];
	}
	for (int i = 0; i < n; i++) {
		for (const auto& j : str[i]) {
			if (j=='d') {
				if (d == 1) {
					cout << "q";
				}
				else {
					cout << "b";
				}
			}
			else if (j=='b') {
				if (d == 1) {
					cout << "p";
				}
				else {
					cout << "d";
				}
			}
			else if (j == 'q') {
				if (d == 1) {
					cout << "d";
				}
				else {
					cout << "p";
				}
			}
			else if (j == 'p') {
				if (d == 1) {
					cout << "b";
				}
				else {
					cout << "q";
				}
			}
		}
		cout << "\n";
	}
}