#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int area = brown+yellow;
    for(int i=1;i<=area;i++){
        int w=area/i;
        if(i>w){
            break;
        }
        if(area%i!=0){
            continue;
        }
        if(w*2+(i-2)*2==brown){
            answer.push_back(w);
            answer.push_back(i);
            break;
        }
    }
    return answer;
}