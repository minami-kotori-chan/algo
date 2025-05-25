#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> arr;
    for(const auto& c : commands){
        arr.clear();
        for(int i=c[0]-1;i<c[1];i++){
            arr.push_back(array[i]);
        }
        sort(arr.begin(),arr.end());
        answer.push_back(arr[c[2]-1]);
    }
    return answer;
}