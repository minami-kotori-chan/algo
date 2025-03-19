#include <iostream>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    int a,b;
    cin>>a>>b;

    if(a==b){
        cout<<"==";
    }
    else if(a>b){
        cout<<">";
    }
    else{
        cout<<"<";
    }
    
    return 0;
}