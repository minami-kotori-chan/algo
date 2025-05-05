#include <iostream>
#include <string>
using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int main(void) {
	FAST_IO;
	int arr[26] = { 0, };
	int pass_count[26] = { 0, };
	int n,m;
	string str;

	cin >> n>>m;
	cin >> str;

	for (char i : str) {
		arr[i - 'a']++;
	}
	int sub = m;
	for (int i = 0; i < m;i++) {
		for (int j = 0; j < 26; j++) {
			if (arr[j] != 0) {
				arr[j]--;
				pass_count[j]++;
				break;
			}
		}
	}

	int result_count[26] = { 0, };
	for (char i : str) {
		if (pass_count[i - 'a'] > result_count[i - 'a']) {
			result_count[i - 'a']++;
			continue;
		}
		cout << i;
	}
	return 0;
}