#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int st1[]={1,2,3,4,5};
    int st2[]={2,1,2,3,2,4,2,5};
    int st3[]={3,3,1,1,2,2,4,4,5,5};
    int scores[4]={0,};
    
    for(int i=0;i<answers.size();i++){
        if(answers[i]==st1[i%5]) scores[1]++;
        if(answers[i]==st2[i%8]) scores[2]++;
        if(answers[i]==st3[i%10]) scores[3]++;
    }
    int mx=0;
    for(int i=1;i<=3;i++){
        if(scores[i]>mx){
            mx=scores[i];
        }
    }
    for(int i=1;i<=3;i++){
        if(scores[i]==mx){
            answer.push_back(i);
        }
    }
    
    return answer;
}