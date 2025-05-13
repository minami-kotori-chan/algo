#include <iostream>
#include <vector>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    int t;
    cin>>t;
    vector<vector<int>> arr;
    int counter[100]={0,};
    int result=-1;
    for(int testcase=0;testcase<t;testcase++){
        int c,v;
        cin>>c>>v;
        arr.clear();
        for(int i=0;i<100;i++){
            counter[i]=0;
        }
        for(int i=0;i<v;i++){
            arr.push_back(vector<int>(c));
            for(int j=0;j<c;j++){
                int temp;
                cin>>temp;
                arr[i][temp-1]=j;
                if(j==0){
                    counter[temp-1]++;
                }
            }
        }
        
        
        pair<int,int> num1={0,0},num2={0,0};
        
        for(int i=0;i<c;i++){
            if(counter[i]>num1.first){
                num1.first=counter[i];
                num1.second=i;
            }
        }
        for(int i=0;i<c;i++){
            if(num1.second==i){
                continue;
            }
            if(counter[i]>num2.first){
                num2.first=counter[i];
                num2.second=i;
            }
        }
        if(num1.first>v/2){
            cout<<num1.second+1<<" 1"<<"\n";
            continue;
        }
        num1.first=0;
        num2.first=0;
        for(int i=0;i<v;i++){
            if(arr[i][num1.second]>arr[i][num2.second]){
                num2.first++;
            }
            else{
                num1.first++;
            }
            
        }
        if(num1.first>num2.first){
            cout<<num1.second+1<<" 2";
        }
        else{
            cout<<num2.second+1<<" 2";
        }
        cout<<"\n";

    }

    return 0;
}