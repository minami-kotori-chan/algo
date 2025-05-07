#include <iostream>
#include <deque>
#include <string>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    int n;
    cin>>n;
    deque<pair<string,int>> que;

    for(int i=0;i<n;i++){
        string name;
        int num;
        cin>>name>>num;
        que.push_back({name,num});
    }
    while(que.size()>2){
        pair<string,int> temp=que.front();
        que.pop_front();
        for(int i=1;i<temp.second;i++){
            que.push_back(que.front());
            que.pop_front();
        }
        que.pop_front();
    }
    cout<<que.front().first;

    return 0;
}