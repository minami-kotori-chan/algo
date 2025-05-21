#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

bool compare(const pair<int,int>& a,const pair<int,int>& b){
    if(a.first+a.second!=b.first+b.second) return a.first+a.second<b.first+b.second;
    return a.first<b.first;
}

int main(void){
    fast_io;
    int n,b;
    cin>>n>>b;
    vector<pair<int,int>> arr(n);
    for(auto& i : arr){
        cin>>i.first>>i.second;
    }
    sort(arr.begin(),arr.end(),compare);
    long long int result=0;
    int count=0;
    int max_value=arr[0].first;
    while(result<=b){
        result+=arr[count].first+arr[count].second;
        count++;
        max_value=max(arr[count].first,max_value);
    }
    if(result-(max_value-max_value/2)>b){
        count--;
    }

    cout<<count;
    return 0;
}