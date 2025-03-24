#include <iostream>
#include <vector>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    int n,x;
    cin>>n>>x;
    vector<int> vc(n);
    for(int i=0;i<n;i++){
        cin>>vc[i];
        if (vc[i]<x){
            cout<<vc[i]<<" ";
        }
    }
}