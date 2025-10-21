#include <iostream>
#include <vector>

using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    int n,m,q;
    cin>>n>>m>>q;
    vector<vector<int>> map(n+1,vector<int>());
    vector<int> v(n+1,0);
    vector<int> visit(n+1,0);
    for(int i=1;i<=n;i++){
        map[i].push_back(i);
    }
    for(int i=0;i<m;i++){
        int a,b;
        cin>>a>>b;
        map[a].push_back(b);
        map[b].push_back(a);
    }
    for(int i=0;i<q;i++){
        int number;
        int count=0;
        cin>>number;
        if(visit[number]!=1){
            for(const auto& j : map[number]){
                if(v[j]==0){
                    count++;
                    v[j]=1;
                }
            }
            visit[number]=1;
            cout<<count<<"\n";
        }
        else{
            cout<<0<<"\n";
        }
    }
    
    return 0;
}