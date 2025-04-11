#include <iostream>
#include <deque>
using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int graph[500][500] = { 0, };
int n, m;
int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };
deque<pair<int,int>> stack;
int visited[500][500] = { 0, };
int output = 0;

int calc_value() {
	int result = 0;
	for (auto i : stack) {
		result += graph[i.first][i.second];
	}
	return result;
}

void dfs(int row,int col, int depth = 1) {
	if (depth == 1) {
		visited[row][col] = 1;
		stack.push_back({ row,col });

	}
	if (depth == 4) {
		output = max(calc_value(), output);
		return;
	}
	int r, c;
	for (int i = 0; i < 4; i++) {
		r = row + dr[i];
		c = col + dc[i];
		if (r >= n || r < 0 || c >= m || c < 0)
			continue;
		if (visited[r][c] == 1)
			continue;
		visited[r][c] = 1;
		stack.push_back({ r,c });
		dfs( r, c, depth + 1);
		stack.pop_back();
		visited[r][c] = 0;
	}
	if (depth == 1) {
		visited[row][col] = 0;
		stack.pop_back();
	}
}
void get_oshape(int row,int col) {
	int r, c;
	int result = 0;
	for (int i = 0; i < 4; i++) {
		result = graph[row][col];
		for (int j = 0; j < 4; j++) {
			if (i == j) {
				continue;
			}
			r = row + dr[j];
			c = col + dc[j];
			if (r >= n || r < 0 || c >= m || c < 0) {
				result = 0;
				break;
			}
			result += graph[r][c];
		}
		output = max(output, result);
	}
}

int main(void) {
	FAST_IO;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> graph[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			dfs(i, j);
			get_oshape(i, j);
		}
	}
	cout << output;
	return 0;
}