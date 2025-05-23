#include <string>
#include <vector>
#include <deque>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    deque<int> que;
    for(int i=0;i<progresses.size();i++){
        int num=(100-progresses[i])/speeds[i];
        if((100-progresses[i])%speeds[i]!=0){
            num++;
        }
        que.push_back(num);
        
    }
    while(!que.empty()){
        int cur = que.front();
        que.pop_front();
        answer.push_back(1);
        while(!que.empty()&&cur>=que.front()){
            que.pop_front();
            answer[answer.size()-1]++;
        }
        
    }
    return answer;
}