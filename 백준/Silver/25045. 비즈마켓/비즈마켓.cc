#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    vector<int> a;
    vector<int> b;
    int n,m;
    cin>>n>>m;
    for(int i=0;i<n;i++){
        int temp;
        cin>>temp;
        a.push_back(temp);
    }
    for(int i=0;i<m;i++){
        int temp;
        cin>>temp;
        b.push_back(temp);
    }
    sort(a.begin(),a.end(),[](int a,int b){return a>b;});
    sort(b.begin(),b.end(),[](int a,int b){return a<b;});

    int k = min(n,m);
    long long int result=0;
    for(int i=0;i<k;i++){
        if(a[i]>b[i]){
            result+=(a[i]-b[i]);
        }
    }
    cout<<result;
    return 0;
}