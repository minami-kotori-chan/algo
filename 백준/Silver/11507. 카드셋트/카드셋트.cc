#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);


int main(void){
    fast_io;
    string str;
    cin>>str;
    vector<unordered_set<string>> vc(4);
    int result=0;
    for(int i=0;i<str.size();i+=3){
        string tmp;
        for(int j=i;j<i+3;j++){
            tmp+=str[j];
        }
        
        int vc_num=0;
        if(str[i]=='P'){
            vc_num=0;
        }
        else if(str[i]=='K'){
            vc_num=1;
        }
        else if(str[i]=='H'){
            vc_num=2;
        }
        else if(str[i]=='T'){
            vc_num=3;
        }
        
        if(vc[vc_num].find(tmp)==vc[vc_num].end()){
            vc[vc_num].insert(tmp);
        }
        else{
            result=-1;
            break;
        }
    }
    
    if(result==-1){
        cout<<"GRESKA";
    }
    else{
        for(int i=0;i<4;i++){
            cout<<13-vc[i].size()<<" ";
        }
    }

    return 0;
}