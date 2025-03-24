#include <iostream>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    long long int n,m;
    long long int result;
    cin>>n>>m;
    result=n-m;
    if (result<0){
        cout<<-result;
    }
    else{
        cout<<result;
    }
}