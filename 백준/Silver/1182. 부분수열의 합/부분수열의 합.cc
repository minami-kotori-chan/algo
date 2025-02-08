#include <iostream>
#include <vector>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int n, s;
int result = 0;
vector<int> stack;
vector<int> stack_index;
vector<int> vc;
vector<int> v;

int calc_sum() {
	int sum = 0;
	for (const auto& i : stack)
		sum += i;
	return sum;
}

void dfs(int l=0) {
	if ( l!=0 && stack.size() == l) {
		if (calc_sum() == s) {
			result++;
		}
		return;
	}
	if (l == 0) {
		for (int i = 1; i < n + 1; i++) {
			for (int j = 0; j < n; j++) {
				if (v[j] == 1 || (stack_index.size()>0 && stack_index[stack_index.size()-1]>j))
					continue;
				v[j] = 1;
				stack.push_back(vc[j]);
				stack_index.push_back(j);
				dfs(i);
				stack_index.pop_back();
				stack.pop_back();
				v[j] = 0;
			}
		}
	}
	else {
		for (int j = 0; j < n; j++) {
			if (v[j] == 1 || (stack_index.size() > 0 && stack_index[stack_index.size() - 1] > j))
				continue;
			v[j] = 1;
			stack.push_back(vc[j]);
			stack_index.push_back(j);
			dfs(l);
			stack_index.pop_back();
			stack.pop_back();
			v[j] = 0;
		}
	}
}

int main(void) {
	FAST_IO;
	cin >> n >> s;


	for (int i = 0; i < n; i++) {
		int input_temp;
		cin >> input_temp;
		vc.push_back(input_temp);
		v.push_back(0);
	}

	dfs();

	cout << result;
}