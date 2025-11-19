#include <iostream>
#include <string>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    int n;
    cin>>n;
    string str;
    cin>>str;
    int s_c=0;
    int l_c=0;
    int result=0;
    bool is_valid=true;
    for(const auto& i : str){
        if(!is_valid) continue;
        if(i>='1' && i<='9'){
            result++;
            continue;
        }
        else if(i=='S'){
            s_c++;
        }
        else if(i=='L'){
            l_c++;
        }
        else if(i=='K'){
            if(s_c>0){
                s_c--;
                result++;
            }
            else{
                is_valid=false;
            }
        }
        else if(i=='R'){
            if(l_c>0){
                l_c--;
                result++;
            }
            else{
                is_valid=false;
            }
        }
    }
    cout<<result;

    return 0;
}