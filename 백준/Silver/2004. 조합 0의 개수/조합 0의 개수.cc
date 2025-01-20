#include <iostream>

using namespace std;

int fact_zero(const int& n,const int& m) {
	int result = 0;
	int count_n[2] = {0};
	int count_m[2] = {0};


	for (long long j = 2; j <= n; j*=2) {
		count_n[0] += n / j;
	}
	for (long long j = 5; j <= n; j *= 5) {
		count_n[1] += n / j;
	}
	for (long long j = 2; j <= m; j *= 2) {
		count_m[0] += m / j;
	}
	for (long long j = 5; j <= m; j *= 5) {
		count_m[1] += m / j;
	}
	for (long long j = 2; j <= n-m; j *= 2) {
		count_m[0] += (n-m) / j;
	}
	for (long long j = 5; j <= n-m; j *= 5) {
		count_m[1] += (n-m) / j;
	}

	result=min(count_n[0] - count_m[0],count_n[1]-count_m[1]);

	if (result < 0) {
		result = 0;
	}

	return result;
}

int main(void) {
	int n,m;
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	cin >> n>>m;
	cout<<fact_zero(n,m);
	
	return 0;
}