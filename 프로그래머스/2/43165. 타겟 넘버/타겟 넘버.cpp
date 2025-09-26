#include <string>
#include <vector>

using namespace std;

int result=0;

void dfs(vector<int>& numbers,const int& target,int sum,int n)
{
    if(n==numbers.size()){
        if(target==sum) result++;
        return;
    }
    dfs(numbers,target,sum+numbers[n],n+1);
    dfs(numbers,target,sum-numbers[n],n+1);
}

int solution(vector<int> numbers, int target) {
    int answer=0;
    dfs(numbers,target,0,0);
    answer = result;
    return answer;
}