#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int size=brown+yellow;
    for(int i=1;i<=size;i++){
        if(size%i!=0) continue;
        int w = size/i;
        if(brown==(w*2+(i-2)*2)){
            answer.push_back(w);
            answer.push_back(i);
            break;
        }
    }
    return answer;
}