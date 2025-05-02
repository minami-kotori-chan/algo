#include <iostream>
#include <deque>
#include <vector>
using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int main(void) {
	FAST_IO;
	int  f, s, g, u, d;
	cin >> f >> s >> g >> u >> d;
	int result = -1;
	deque<pair<int,int>> que;
	que.push_back({s,0});
	vector<int> visited(f+1);
	visited[s] = 1;
	while (!que.empty()) {
		pair<int,int> temp = que.front();
		que.pop_front();
		if (temp.first == g) {
			result = temp.second;
			break;
		}
		int up = temp.first + u;
		int down = temp.first - d;
		if (up <= f && visited[up] == 0) { 
			que.push_back({ up,temp.second + 1 }); 
			visited[up] = 1;
		}
		if (down > 0 && visited[down] == 0) { 
			que.push_back({ down,temp.second + 1 }); 
			visited[down] = 1;
		}
		
	}
	if (result == -1) {
		cout << "use the stairs";
	}
	else {
		cout << result;
	}
	return 0;
}