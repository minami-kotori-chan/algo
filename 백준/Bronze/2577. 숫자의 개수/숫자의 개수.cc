#include <iostream>
#include <string>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    string str;
    int arr[10]={0,};
    int a,b,c,result;
    cin>>a>>b>>c;
    result=a*b*c;
    str=to_string(result);
    for(const char& i : str){
        arr[i-'0']++;
    }
    for(const int i : arr){
        cout<<i<<"\n";
    }
    return 0;
}