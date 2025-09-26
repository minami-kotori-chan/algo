#include <string>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

int is_prime(int x)
{
    if(x<2) return 0;
    for(int i=2;i<x;i++){
        if(x%i==0) return 0;
    }
    return 1;
}
int solution(string numbers) 
{
    int answer = 0;
    string number = numbers;
    unordered_set<int> set;
    sort(number.begin(),number.end());
    do{
        string tmp;
        for(int i=0;i<number.size();i++){
            tmp+=number[i];
            if(set.find(stoi(tmp))==set.end()){
                if(is_prime(stoi(tmp))){
                    set.insert(stoi(tmp));
                }
            }
        }
    }while(next_permutation(number.begin(),number.end()));
    answer=set.size();
    return answer;
}