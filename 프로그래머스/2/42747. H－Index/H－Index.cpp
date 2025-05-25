#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    sort(citations.begin(),citations.end());
    
    for(int i=0;i<=citations[citations.size()-1];i++){
        int count=0;
        int count2=0;
        for(const auto& j : citations){
            if(j>=i){
                count++;
            }
            else{
                count2++;
            }
        }
        if(count>=i && count2<=i){
            answer=i;
        }
    }
    return answer;
    
    
}