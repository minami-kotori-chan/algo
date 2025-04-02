#include <iostream>

using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    int n;
    cin>>n;

    if(n%7==2) cout<<1;
    else cout<<0;
    return 0;
}