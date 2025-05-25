#include <string>
#include <vector>
#include <iostream>

using namespace std;
vector<int> arr;
vector<int> int_word;
int count=0;
int res;
bool found=false;
void dfs(){
    if(arr.size()==int_word.size()){
        bool result=true;
        for(int i=0;i<int_word.size();i++){
            if(arr[i]!=int_word[i]){
                result=false;
                break;
            }
        }
        if(result){
            found=true;
            res=count;
        }
    }
    if(arr.size()==5){
        return;
    } 
    for(int i=1;i<=5;i++){
        arr.push_back(i);
        count++;
        dfs();
        arr.pop_back();
        if(found==true) return;
    }
}
int solution(string word) {
    int answer = 0;
    
    for(const auto& i : word){
        if(i=='A') int_word.push_back(1);
        else if(i=='E') int_word.push_back(2);
        else if(i=='I') int_word.push_back(3);
        else if(i=='O') int_word.push_back(4);
        else int_word.push_back(5);
    }
    dfs();
    answer=res;
    return answer;
}