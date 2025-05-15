#include <iostream>

using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    int a,b;
    int n,m;
    cin>>a>>b>>n>>m;
    int result_a,result_b;
    result_b=b*m;
    result_a=a*m+b*n;
    int r;
    while(true){
        r = result_b%result_a;
        if(r==0) break;
        result_b=result_a;
        result_a=r;
    }
    cout<<(a*m+b*n)/result_a<<" "<<(b*m)/result_a;
    return 0;
}