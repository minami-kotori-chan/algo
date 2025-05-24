#include <string>
#include <vector>
#include <deque>
#include <iostream>
using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    deque<pair<int,int>> que;
    vector<int> data(priorities);
    
    for(int i=0;i<priorities.size();i++){
        que.push_back({priorities[i],i});
    }
    int index=1;
    while(!que.empty()){
        int num=que.front().first;
        int result=0;
        
        for(const auto& i : que){
            if(num<i.first){
                que.push_back(que.front());
                que.pop_front();
                result=1;
                break;
            }
        }
        if(result==0){
            int num_second=que.front().second;
            que.pop_front();
            data[num_second]=index;
            index++;
        }
        
    }
    answer=data[location];
    return answer;
}