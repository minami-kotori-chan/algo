#include <string>
#include <vector>

using namespace std;

int dfs(vector<vector<int>>& com,int& index,vector<int>& v)
{
    if(v[index]==1) return 0;
    v[index]=1;
    for(int i=0;i<com[index].size();i++){
        if(index==i) continue;
        if(com[index][i]==1){
            dfs(com,i,v);
        }
    }
    return 1;
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<int> v(n);
    
    for(int i=0;i<n;i++){
        answer+=dfs(computers,i,v);    
    }
    
    return answer;
}