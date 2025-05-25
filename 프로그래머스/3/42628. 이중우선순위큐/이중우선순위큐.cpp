#include <string>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    priority_queue<int> max_pq;
    priority_queue<int,vector<int>,greater<int>> min_pq;
    unordered_map<int,int> hash_data;
    int size=0;
    for(const auto& i : operations){
        char opcode = i.substr(0,1)[0];
        int num = stoi(i.substr(2));
        if(opcode=='I'){
            max_pq.push(num);
            min_pq.push(num);
            hash_data[num]++;
            size++;
        }
        else{
            if(num==1){
                if(!max_pq.empty()) {
                    hash_data[max_pq.top()]--;
                    max_pq.pop();
                    size--;
                }
            }
            else{
                if(!min_pq.empty()) {
                    hash_data[min_pq.top()]--;
                    min_pq.pop();
                    size--;
                }
            }
        }
        if(size==0){
            while(!min_pq.empty()){
                min_pq.pop();
            }
            while(!max_pq.empty()){
                max_pq.pop();
            }
        }
    }
    
    if(size!=0){
        while(hash_data[max_pq.top()]==0){
            max_pq.pop();
        }
        while(hash_data[min_pq.top()]==0){
            min_pq.pop();
        }
        answer.push_back(max_pq.top());
        answer.push_back(min_pq.top());
    }
    else{
        answer.push_back(0);
        answer.push_back(0);
    }
    return answer;
}