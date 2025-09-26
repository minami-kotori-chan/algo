#include <vector>
#include <deque>
using namespace std;

int solution(vector<vector<int>> maps)
{
    int answer = -1;
    deque<pair<pair<int,int>,int>> que;
    vector<vector<int>> v;
    for(int i=0;i<maps.size();i++){
        v.push_back(vector<int>(maps[i].size()));
    }
    int dc[]={1,0,-1,0};
    int dr[]={0,-1,0,1};
    que.push_back({{0,0},1});
    v[0][0]=1;
    while(!que.empty()){
        pair<pair<int,int>,int> cur = que.front();
        que.pop_front();
        int row=cur.first.first,col=cur.first.second;
        int cnt = cur.second;
        if(row==maps.size()-1 && col==maps[0].size()-1){
            answer=cnt;
            return answer;
        }
        for(int i=0;i<4;i++){
            int r=row+dr[i];
            int c=col+dc[i];
            if(c<0 || c>=maps[0].size() || r<0 || r>=maps.size()){
                continue;
            }
            if(maps[r][c]==0) continue;
            if(v[r][c]==1) continue;
            if(c==maps[0].size()-1 && r==maps.size()-1){
                answer = cnt+1;
                return answer;
            }
            que.push_back({{r,c},cnt+1});
            v[r][c]=1;
        }
    }
    
    return answer;
}