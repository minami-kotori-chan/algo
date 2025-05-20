#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;
#define fast_io cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);

typedef struct student{
    string name;
    int score;
    int risk;
    int cost;
    int full;
}student;

bool compare(student a,student b){
    if(a.full!=b.full) return a.full>b.full;
    if(a.cost!=b.cost) return a.cost<b.cost;
    return a.name<b.name;
}

int main(void){
    fast_io;
    int n;
    cin>>n;
    vector<student> arr(n);

    for(int i=0;i<n;i++){
        cin>>arr[i].name>>arr[i].score>>arr[i].risk>>arr[i].cost;
        int up=arr[i].score*arr[i].score*arr[i].score;
        int down=arr[i].cost*(arr[i].risk+1);

        arr[i].full=up/down;
    }

    sort(arr.begin(),arr.end(),compare);

    cout<<arr[1].name;
    return 0;
}