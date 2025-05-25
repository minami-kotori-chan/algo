#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int w=0,h=0;
    for(const auto& i : sizes){
        int area1=max(w,i[0])*max(h,i[1]);
        int area2=max(w,i[1])*max(h,i[0]);
        if(area1>area2){
            w=max(w,i[1]);
            h=max(h,i[0]);
        }
        else{
            w=max(w,i[0]);
            h=max(h,i[1]);
        }
    }
    answer=w*h;
    return answer;
}