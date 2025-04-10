#include <iostream>
#include <vector>
#include <deque>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
int graph[8][8];
deque<pair<int,int>> stack;
int n, m;
int dr[4] = {-1,0,1,0};
int dc[4] = { 0,1,0,-1 };
int v[8][8] = { 0, };
int visited[8][8] = {0,};
int output=0;
int bfs() {
	deque<pair<int,int>> que;
	
	

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			v[i][j] = 0;
			if (graph[i][j] == 2) {
				que.push_back({ i,j });
				v[i][j] = 1;
			}
		}
	}
	
	while (que.size())
	{
		pair<int, int> p;
		int row, col;
		p=que.front();
		que.pop_front();
		
		for (int i = 0; i < 4; i++){
			row = p.first+dr[i]; col = p.second+dc[i];

			if (row >= n || row < 0 || col >= m || col < 0)
				continue;
			if (graph[row][col] == 1 || v[row][col]==1)
				continue;
			v[row][col] = 1;
			que.push_back({ row,col });

		}
	}
	int result = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (v[i][j] == 0 && graph[i][j] == 0) {
				result++;
			}
		}
	}
	return result;
}

void dfs() {
	if (stack.size() == 3) {
		output=max(bfs(),output);
		return;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (!stack.empty() && i * n + j < stack.back().first * n + stack.back().second)
				continue;
			if (visited[i][j] == 1)
				continue;
			if (graph[i][j] != 0)
				continue;
			stack.push_back({ i,j });
			visited[i][j] = 1;
			graph[i][j] = 1;
			dfs();
			graph[i][j] = 0;
			visited[i][j] = 0;
			stack.pop_back();
		}
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
	dfs();
	cout << output;

	return 0;
}