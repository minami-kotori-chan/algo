#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    int n;
    vector<int> arr;
    cin>>n;
    for(int i=0;i<n;i++){
        int temp;
        cin>>temp;
        arr.push_back(temp);
    }
    sort(arr.begin(),arr.end(),[](int a,int b){return a>b;});
    double result=arr[0];
    for(int i=1;i<n;i++){
        result+=(arr[i])/2.0;
    }
    
    cout<<result;
    return 0;
}