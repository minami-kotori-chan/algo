#include <string>
#include <deque>
#include <iostream>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    deque<char> stack;
    
    for(const auto& i:s){
        if(i=='('){
            stack.push_back(i);
            continue;
        }
        if(stack.size()==0 || stack.back()!='('){
            answer=false;
            break;
        }
        else{
            stack.pop_back();
        }
    }
    if(!stack.empty()){
        answer=false;
    }


    return answer;
}