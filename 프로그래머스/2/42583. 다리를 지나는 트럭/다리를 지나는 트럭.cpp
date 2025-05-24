#include <string>
#include <vector>
#include <deque>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    deque<int> que1;
    
    for(const auto& i : truck_weights){
        que1.push_back(i);
    }
    
    deque<pair<int,int>> que2;
    int que_sum=0;
    int sec=0;
    
    while(!que1.empty() || !que2.empty()){
        sec++;
        if(!que2.empty() && sec-que2.front().second>=bridge_length){
            que_sum-=que2.front().first;
            que2.pop_front();
            
        }
        if(!que1.empty() && que_sum+que1.front()<=weight && que2.size()<bridge_length){
            que2.push_back({que1.front(),sec});
            que_sum+=que1.front();
            que1.pop_front();
        }
        
    }
    answer=sec;
    return answer;
}