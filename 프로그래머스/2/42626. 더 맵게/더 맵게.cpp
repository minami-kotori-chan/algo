#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    priority_queue<int,vector<int>,greater<int>> pq;
    int answer = 0;
    for(const auto& i : scoville){
        pq.push(i);
    }
    while(pq.size()>=2 && pq.top()<K){
        int first=pq.top();
        pq.pop();
        int second=pq.top();
        pq.pop();
        pq.push(first+second*2);
        answer++;
    }
    if(pq.top()<K) answer=-1;
    return answer;
}