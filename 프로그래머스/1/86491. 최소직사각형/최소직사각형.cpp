#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int w=min(sizes[0][0],sizes[0][1]),h=max(sizes[0][0],sizes[0][1]);
    for(const auto& size : sizes){
        h=max(max(size[0],size[1]),h);
        w=max(min(size[0],size[1]),w);
    }
    answer=w*h;
    return answer;
}