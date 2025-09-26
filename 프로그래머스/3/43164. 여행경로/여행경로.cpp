#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> stack;
int result = 0;
void dfs(vector<vector<string>>& tickets,vector<int>& v,string search)
{
    if(stack.size()==tickets.size()+1)
    {
        result=1;
        return;
    }
    
    for(int i=0;i<tickets.size();i++){
        if(tickets[i][0]==search){
            if(v[i]==1) continue;
            stack.push_back(tickets[i][1]);
            v[i]=1;
            dfs(tickets,v,tickets[i][1]);
            if(result==1) return;
            v[i]=0;
            stack.pop_back();
        }
    }
    
}

vector<string> solution(vector<vector<string>> tickets) {
    vector<int> v(tickets.size());
    sort(tickets.begin(),tickets.end());
    stack.push_back("ICN");
    dfs(tickets,v,"ICN");
    return stack;
}