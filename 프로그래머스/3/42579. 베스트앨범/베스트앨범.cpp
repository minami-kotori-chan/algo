#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <iostream>
using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map<string,vector<pair<int,int>>> hash_data;
    unordered_map<string,int> hash_count;
    vector<pair<string,int>> temp_arr;
    for(int i=0;i<genres.size();i++){
        hash_count[genres[i]]+=plays[i];
        hash_data[genres[i]].push_back({plays[i],i});
    }
    for(const auto& i : hash_count){
        temp_arr.push_back({i.first,i.second});
    }
    sort(temp_arr.begin(),temp_arr.end(),[](const auto& a,const auto& b){return a.second>b.second;});
    for(const auto& i : temp_arr){
        sort(hash_data[i.first].begin(),hash_data[i.first].end(),[](const auto& a,const auto& b){return a.first>b.first;});
        for(int j=0;j<2 && j<hash_data[i.first].size();j++){
            answer.push_back(hash_data[i.first][j].second);
        }
    }
    return answer;
}