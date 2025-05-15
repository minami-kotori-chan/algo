#include <iostream>
#include <vector>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);
int arr[5][5];
vector<int> que;
int result=0;
int visit[5][5]={0,};
int dr[]={-1,0,1,0};
int dc[]={0,1,0,-1};

void dfs(int row=0,int col=0,int count=0,int depth=0){
    if(visit[row][col]==1) return;
    if(depth>=4) return;
    visit[row][col]=1;
    if(arr[row][col]==-1) return;
    if(arr[row][col]==1) count++;
    
    if(count>=2){
        result=1; 
        return;
    }
    
    for(int i=0;i<4;i++){
        int r=row+dr[i];
        int c=col+dc[i];
        if(r>=5 || r<0 || c>=5||c<0) continue;
        dfs(r,c,count,depth+1);
    }
    visit[row][col]=0;
}

int main(void){
    fast_io;
    
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            cin>>arr[i][j];
        }
    }
    int n,m;
    cin>>n>>m;
    dfs(n,m);

    cout<<result;
    return 0;
}