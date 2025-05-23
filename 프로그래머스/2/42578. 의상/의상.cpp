#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 0;
    unordered_map<string,int> hash_data;
    for(const auto& i : clothes){
        hash_data[i[1]]+=1;
    }
    int result=1;
    for(auto i : hash_data){
        result*=i.second+1;
    }
    answer=result-1;
    
    return answer;
}