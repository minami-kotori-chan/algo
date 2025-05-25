#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    
    int answer = -1;
    vector<int> arr;
    
    for(int i=0;i<dungeons.size();i++){
        arr.push_back(i);
    }
    do{
        int hp=k;
        int result=0;
        for(int i=0;i<dungeons.size();i++){
            if(hp>=dungeons[arr[i]][0]){
                hp-=dungeons[arr[i]][1];
                result++;
            }
            else{
                continue;
            }
        }
        answer=max(answer,result);
    }while(next_permutation(arr.begin(),arr.end()));
    return answer;
}