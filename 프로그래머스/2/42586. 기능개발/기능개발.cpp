#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<pair<int,int>> answer;
    // 7 3 19
    for(int i = 0;i<speeds.size();i++){
        int temp = (100-progresses[i])/speeds[i];
        if((100-progresses[i])%speeds[i] != 0){
            temp++;
        }
        
        if(answer.size()==0 || answer.back().first<temp){
            answer.push_back({temp,1});
            
        }
        else{
            answer.back().second+=1;
        }
    }
    vector<int> result;
    for(const auto& i : answer){
        result.push_back(i.second);
    }
    return result;
}