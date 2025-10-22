#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);


int main(void){
    fast_io;
    int n,s;
    cin>>n;
    vector<int> arr(n);
    vector<int> v(n,0);
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cin>>s;
    queue<int> que;
    que.push(s-1);
    int result=0;
    while(!que.empty()){
        int num = que.front();
        que.pop();
        if(v[num]!=0){
            continue;
        }
        result++;
        v[num]=1;
        if(num+arr[num]<n){
            que.push(num+arr[num]);
        }
        if(num-arr[num]>=0){
            que.push(num-arr[num]);
        }
    }
    cout<<result;

    return 0;
}