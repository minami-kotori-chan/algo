#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    int n,k;
    int result=0;
    int arr[6][2]={0,};
    cin>>n>>k;

    for(int i=0;i<n;i++){
        int s,y;
        cin>>s>>y;
        arr[y-1][s]++;
    }
    for(int i=0;i<6;i++){
        for(int j=0;j<2;j++){
            if(arr[i][j]==0){
                continue;
            }
            result+=arr[i][j]/k;
            if(arr[i][j]%k!=0){
                result++;
            }
        }
    }
    cout<<result;
    return 0;
}