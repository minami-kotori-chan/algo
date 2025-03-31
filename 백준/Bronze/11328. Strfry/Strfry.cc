#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    int n;
    
    cin>>n;
    for(int i=0;i<n;i++){
        string str1,str2;
        int arr1[26]={0,};
        int arr2[26]={0,};
        cin>>str1>>str2;

        bool result=true;

        for(int i:str1){
            arr1[i-'a']++;
        }
        for(int i:str2){
            arr2[i-'a']++;
        }
        for(int i=0;i<26;i++){
            if(arr1[i]!=arr2[i]){
                result=false;
                break;
            }
        }
        if(result){
            cout<<"Possible";
        }
        else{
            cout<<"Impossible";
        }
        cout<<"\n";
    }
    
    return 0;
}