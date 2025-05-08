#include <iostream>
#include <vector>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int main(void){
    fast_io;
    int n;
    long long k;
    cin >> n >> k;
    vector<int> arr;
    long long int sum=0;
    int result = 0;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        arr.push_back(temp);
        sum += temp;
    }
    
    if (k > sum) {
        k -= sum;
        for (int i = arr.size()-1; i >=0; i--) {
            result = i;
            if (arr[i] > k) {
                break;
            }
            k -= arr[i];
        }
    }
    else {
        for (int i = 0; i < arr.size(); i++) {
            result = i;
            if (arr[i] > k) {
                break;
            }
            k -= arr[i];
        }
    }
    
    cout << result+1;
}
