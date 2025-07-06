#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int arr[10000] = { 0, };

int main(void) {
	FAST_IO;
	
	int n, m;
	cin >> n >> m;

	vector<vector<int>> vc(n,vector<int>(m,0));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> vc[i][j];
		}
	}
	vector<vector<int>> comp;
	vector<int> tmp, uni;
	for (int i = 0; i < n; i++) {
		tmp.clear();
		uni.clear();
		comp.push_back(vector<int>());
		for (int j = 0; j < m; j++) {
			tmp.push_back(vc[i][j]);
		}
		sort(tmp.begin(), tmp.end());
		for (int j = 0; j < m; j++) {
			if (j==0 || tmp[j] != tmp[j - 1]) {
				uni.push_back(tmp[j]);
			}
		}
		for (int j = 0; j < m; j++) {
			comp[i].push_back(lower_bound(uni.begin(), uni.end(), vc[i][j]) - uni.begin());
		}
		cout << "";
	}
	int result = 0;

	for (int i = 0; i < n-1; i++) {
		for (int j = i+1; j < n; j++) {
			int flag = 0;
			for (int k = 0; k < m; k++) {
				if (comp[i][k] != comp[j][k]) {
					flag = 1;
					break;
				}
			}
			if (flag == 0) {
				result++;
			}
		}
	}
	cout << result;
	return 0;
}