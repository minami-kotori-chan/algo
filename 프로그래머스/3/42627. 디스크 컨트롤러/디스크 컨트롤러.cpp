#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

struct wdata{
    int id;
    int req;
    int time;
};

struct cmp{
    bool operator()(wdata& a,wdata& b){
        if(a.time!=b.time) return a.time>b.time;
        if(a.req!=b.req) return a.req>b.req;
        return a.id>b.id;
    }
};
struct wait_cmp{
    bool operator()(wdata& a,wdata& b){
        return a.req>b.req;
    }
};


int solution(vector<vector<int>> jobs) {
    int answer = 0;
    priority_queue<wdata,vector<wdata>,cmp> pq;
    priority_queue<wdata,vector<wdata>,wait_cmp> wait_pq;
    vector<int> comp_time;
    
    for(int i=0;i<jobs.size();i++){
        wait_pq.push({i,jobs[i][0],jobs[i][1]});
    }
    int start_time=0;
    while(!wait_pq.empty() || !pq.empty()){
        while(!wait_pq.empty() && wait_pq.top().req<=start_time){
            pq.push(wait_pq.top());
            wait_pq.pop();
        }
        if(!pq.empty()){
            wdata t = pq.top();
            pq.pop();
            start_time+=t.time;
            comp_time.push_back(start_time-t.req);
            continue;
        }
        start_time++;
    }
    int avg=0;
    for(const auto& i : comp_time){
        avg+=i;
    }
    avg/=comp_time.size();
    answer=avg;
    return answer;
}