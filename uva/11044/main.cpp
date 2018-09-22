#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int n;
	cin>>n;
	while(n--) {
		int w,h;
		cin>>w>>h;
		int res = (w/3) * (h/3);
		cout<<res<<endl;
	}
	return 0;
}
