#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    string str;
    int arr[9]={0,};
    int result=0;
    cin>>str;
    for(const char i : str){
        if (i-'0'==9){
            arr[6]++;
        }
        else{
            arr[i-'0']++;
        }
    }
    arr[6]=arr[6]/2+arr[6]%2;
    for(const int i: arr){
        result=max(result,i);
    }
    cout<<result;
    return 0;
}