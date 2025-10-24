#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int main(void) {
	FAST_IO;
	int b, c, d;
	cin >> b >> c >> d;
	vector<int> buger(b);
	vector<int> side(c);
	vector<int> drink(d);
	int sum = 0;
	for (int i = 0; i < b; i++) {
		cin >> buger[i];
		sum += buger[i];
	}
	for (int i = 0; i < c; i++) {
		cin >> side[i];
		sum += side[i];
	}
	for (int i = 0; i < d; i++) {
		cin >> drink[i];
		sum += drink[i];
	}
	cout << sum<<"\n";
	sort(buger.begin(), buger.end(),greater<int>());
	sort(side.begin(), side.end(), greater<int>());
	sort(drink.begin(), drink.end(), greater<int>());
	int size_ = min({ b,c,d });
	for (int i = 0; i < size_; i++) {
		sum -= buger[i] / 10;
		sum -= side[i] / 10;
		sum -= drink[i] / 10;
	}
	cout << sum;
	return 0;
}