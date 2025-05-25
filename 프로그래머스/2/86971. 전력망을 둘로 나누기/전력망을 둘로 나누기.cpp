#include <string>
#include <vector>
#include <deque>

using namespace std;

int count;
vector<vector<int>> v;

void bfs(int w1,int w2,int n){
    deque<int> que;
    que.push_back(w1);
    vector<int> visited(n+1);
    visited[w1]=1;
    count++;
    while(!que.empty()){
        int cur = que.front();
        que.pop_front();
        for(const auto& i : v[cur]){
            if(cur==w1 && i==w2) continue;
            if(visited[i]==1) continue;
            visited[i]=1;
            count++;
            que.push_back(i);
            
        }
    }
}

int solution(int n, vector<vector<int>> wires) {
    int answer = -1;
    for(int i=0;i<n+1;i++){
        v.push_back(vector<int>());
    }
    
    for(const auto& i : wires){
        v[i[0]].push_back(i[1]);
        v[i[1]].push_back(i[0]);
    }
    for(const auto& w : wires){
        count=0;
        bfs(w[0],w[1],n);
        if(answer==-1){
            answer=abs(n-count*2);
        }
        else{
            answer=min(abs(n-count*2),answer);
        }
        
    }
    return answer;
}