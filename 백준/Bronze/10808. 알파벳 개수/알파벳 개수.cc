#include <iostream>
#include <string>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    string str;
    int arr[26]={0,};
    cin>>str;
    for(const char i : str){
        arr[i-'a']++;
    }
    for(int i : arr){
        cout<<i<<" ";
    }
    return 0;
}