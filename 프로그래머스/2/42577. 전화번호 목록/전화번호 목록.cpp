#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    unordered_set<string> set;
    for(const auto& i : phone_book){
        set.insert(i);
    }
    for(const auto& i : set){
        string temp;
        for(int j = 0;j<i.size()-1;j++){
            temp+=i[j];
            if(set.find(temp)!=set.end()){
                return false;
            }
        }
    }
    return true;
}