#include <string>
#include <vector>
#include <deque>
#include <unordered_map>

using namespace std;

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    unordered_map<string,int> set;
    for(const auto& i : words){
        set.insert({i,0});
    }
    //단순하게 a부터 z까지 교체해보면 되지 않을까?
    //그러고 그게 set에 있으면 que에 넣고 bfs
    deque<pair<string,int>> que;
    que.push_back({begin,0});
    while(!que.empty()){
        pair<string,int> cur = que.front();
        que.pop_front();
        
        for(int i=0;i<cur.first.size();i++){
            string str=cur.first;
            for(char j='a';j<='z';j++){
                str[i]=j;
                if(!(set.find(str)==set.end())){
                    if(set[str]==1) continue;
                    if(str==target) return cur.second+1;
                    que.push_back({str,cur.second+1});
                    set[str]=1;
                }
            }
        }
    }
    return answer;
}