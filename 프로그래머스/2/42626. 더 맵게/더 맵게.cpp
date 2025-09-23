#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int,vector<int>,greater<int>> pq;
    for(const auto& i : scoville){
        pq.push(i);
    }
    int cnt=0;
    while(pq.top() < K){
        cnt++;
        int temp = pq.top();
        pq.pop();
        if(pq.empty()){
            cnt=-1;
            break;
        }
        temp += (pq.top()*2);
        pq.pop();
        pq.push(temp);
    }
    
    return cnt;
}