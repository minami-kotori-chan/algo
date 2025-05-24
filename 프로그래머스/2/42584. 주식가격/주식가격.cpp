#include <string>
#include <vector>
#include <deque>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    deque<int> que;
    for(const auto& i : prices){
        que.push_back(i);
    }
    while(!que.empty()){
        int num=que.front();
        que.pop_front();
        int result=0;
        for(const auto& i : que){
            result++;
            if(num>i){
                break;
            }
        }
        
        answer.push_back(result);
    }
    return answer;
}