#include <vector>
#include <deque>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    for(const auto& i : arr){
        if(answer.empty() || answer.back()!=i){
            answer.push_back(i);
        }
    }
    
    return answer;
}