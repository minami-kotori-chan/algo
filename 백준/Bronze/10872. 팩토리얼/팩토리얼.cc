#include <iostream>

using namespace std;

int fact(const int& n) {
	if (n == 0 || n==1) 
		return 1;
	return n * fact(n - 1);
}

int main(void) {
	int n;
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	cin >> n;
	cout << fact(n);
	
	return 0;
}