#include <string>
#include <vector>

using namespace std;
vector<int> nums;
vector<int> stack;
vector<int> v;
int t;
int result=0;
int sum_stack()
{
    int sum=0;
    for(const auto& i : stack){
        sum+=nums[i];
    }
    return sum;
}

void dfs(int size=0)
{
    if(size==0)
    {
        for(int i=1;i<=nums.size();i++){
            dfs(i);
        }
    }
    else
    {
        if(stack.size()==size){
            if(sum_stack()==t){
                result++;
            }
            return;
        }
        for(int i=0;i<nums.size();i++){
            if(v[i]==1) continue;
            if(!stack.empty() && stack.back()>=i) continue;
            v[i]=1;
            stack.push_back(i);
            dfs(size);
            stack.pop_back();
            v[i]=0;
        }
    }
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    int sum = 0;
    for(const auto& i : numbers){
        nums.push_back(i);
        v.push_back(0);
        sum+=i;
    }
    t=(sum-target)/2;
    dfs();
    answer=result;
    return answer;
}