#include <iostream>
#include <vector>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

int arr[1000 * 10000] = { 0, };

int main(void){
    fast_io;
    int n;
    
    cin >> n;
    vector<int> v;
    
    for (int i = 2; i < 1000 * 10000; i++) {
        if (arr[i] == 1) continue;
        v.push_back(i);
        for (int j = i * 2; j < 1000 * 10000; j += i) {
            arr[j] = 1;
        }

    }
    cout << v[n-1];

    return 0;
}
