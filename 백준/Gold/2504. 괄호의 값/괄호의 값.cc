#include <iostream>
#include <string>
#include <vector>

using namespace std;
#define FAST_IO cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);

int main(void) {
	FAST_IO;
	string str;
	vector<int> stack;
	int result = 0;
	cin >> str;
	int tmp = 1;
	int index = 0;
	for (char i : str) {
		if (i == '(') {
			stack.push_back(2);
			tmp *= 2;
		}
		else if(i == '[') {
			stack.push_back(3);
			tmp *= 3;
		}
		else if (i == ']') {
			if (stack.size()==0 || stack.back() != 3) {
				result = 0;
				break;
			}
			stack.pop_back();
			if (str[index - 1] == '[')
			{
				result += tmp;
				
			}
			tmp /= 3;
		}
		else {
			if (stack.size()==0 || stack.back() != 2) {
				result = 0;
				break;
			}
			stack.pop_back();
			if (str[index - 1] == '(')
			{
				result += tmp;
				
			}
			tmp /= 2;
		}
		index++;
	}
	if (!stack.empty())
	{
		result = 0;
	}
	cout << result;
	return 0;
}