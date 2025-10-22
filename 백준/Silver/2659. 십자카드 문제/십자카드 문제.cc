#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int arr[10000]={0,};

int clock_number(int a,int b,int c,int d)
{
    int n1=a*1000+b*100+c*10+d;//2112
    int n2=b*1000+c*100+d*10+a;//1122
    int n3=c*1000+d*100+a*10+b;//1221
    int n4=d*1000+a*100+b*10+c;//2211
    return min({n1,n2,n3,n4});
}

int main(void){
    fast_io;
    vector<int> in_arr=vector<int>(4);
    for(int i=0;i<4;i++){
        cin>>in_arr[i];
    }
    int count=1;
    for(int i=1;i<10;i++){
        for(int j=1;j<10;j++){
            for(int k=1;k<10;k++){
                for(int l=1;l<10;l++){
                    int num = clock_number(i,j,k,l);
                    if(arr[num]==0){
                        arr[num]=count;
                        count++;
                    }
                }
            }
        }
    }
    cout<<arr[clock_number(in_arr[0],in_arr[1],in_arr[2],in_arr[3])];
    return 0;
}