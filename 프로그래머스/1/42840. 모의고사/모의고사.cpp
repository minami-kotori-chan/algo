#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int an1[5]={1,2,3,4,5};
    int an2[8]={2,1,2,3,2,4,2,5};
    int an3[10]={3,3,1,1,2,2,4,4,5,5};
    int score[3]={0,};
    for(int i=0;i<answers.size();i++){
        if(an1[i%5]==answers[i]){
            score[0]++;
        }
        if(an2[i%8]==answers[i]){
            score[1]++;
        }
        if(an3[i%10]==answers[i]){
            score[2]++;
        }
    }
    int v=max(score[0],max(score[1],score[2]));
    for(int i=0;i<3;i++){
        if(score[i]==v) answer.push_back(i+1);
    }
    return answer;
}