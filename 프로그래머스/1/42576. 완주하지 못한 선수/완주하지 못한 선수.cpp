#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string,int> hash_map1;
    unordered_map<string,int> hash_map2;
    for(const auto& i : completion){
        hash_map1[i];
        hash_map1[i]+=1;
    }
    for(const auto& i : participant){
        hash_map2[i];
        hash_map2[i]+=1;
    }
    for(const auto& i : participant){
        if(hash_map1[i]!=hash_map2[i]){
            answer=i;
        }
    }
    return answer;
}