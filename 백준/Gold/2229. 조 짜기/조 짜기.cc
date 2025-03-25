#include <iostream>
#include <algorithm>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);
int v[1001]={0,};
int arr[1001];
int main(void){
    fast_io;
    int n;
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    v[0]=0;
    v[1]=0;
    for(int i=2;i<=n;i++){
        int Max=arr[i];
        int Min=arr[i];
        for(int j=i-1;j>=0;j--){
            Max=max(Max,arr[j+1]);
            Min=min(Min,arr[j+1]);
            v[i]=max(v[i],v[j]+Max-Min);
        }
    }
    cout<<v[n];
    return 0;
}