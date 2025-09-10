#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string,int> hash;
    for(const auto& i : participant){
        if(hash.find(i)==hash.end()){
            hash[i]=1;
        }
        else{
            hash[i]+=1;
        }
    }
    for(const auto& i : completion){
        hash[i]--;
    }
    for(const auto& i : hash){
        if(hash[i.first]!=0){
            answer=i.first;
        }
    }
    return answer;
}