#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    unordered_map<int,int> hash_data;
    for(const auto& i : nums){
        hash_data[i]=1;
    }
    answer=hash_data.size();
    if(answer>nums.size()/2) answer=nums.size()/2;
    return answer;
}