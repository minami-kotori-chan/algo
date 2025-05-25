#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

bool is_prime(int n){
    bool result=true;
    if(n==1 || n==0) return false;
    for(int i=2;i<n;i++){
        if(n%i==0){
            result=false;
            break;
        }
    }
    return result;
}
int solution(string numbers) {
    int answer = 0;
    vector<int> arr;
    unordered_map<int,int> prime_data;
    for(const auto& i : numbers){
        arr.push_back(i-'0');
    }
    sort(arr.begin(), arr.end());
    do{
        string temp;
        for(int i=0;i<arr.size();i++){
            temp+=to_string(arr[i]);
            int val=stoi(temp);
            if(prime_data[val]!=1 && is_prime(val)){
                prime_data[val]=1;
                answer++;
            }
        }
    }while(next_permutation(arr.begin(),arr.end()));
    return answer;
}