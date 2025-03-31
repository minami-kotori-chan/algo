#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    int n,x;
    int result=0;
    cin>>n;
    vector<int> vc(2000001);
    vector<int> arr(n);
    for(int i=0;i<n;i++){
        cin>>arr[i];
        vc[arr[i]]++;
    }
    cin>>x;
    for(int i: arr){
        if(x-i>=0 && vc[x-i]>0){
            result++;
        }
    }
    cout<<result/2;
    return 0;
}