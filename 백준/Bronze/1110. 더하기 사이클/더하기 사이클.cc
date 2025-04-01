#include <iostream>

using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    int n,x=-1;
    int count=1;
    cin>>n;
    x=((n%10)*10)+((n%10+n/10)%10);
    while(n!=x){
        x=((x%10)*10)+((x%10+x/10)%10);
        count++;
    }
    cout<<count;
    return 0;
}