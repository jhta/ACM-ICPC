#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int n, i = 1;
	cin>>n;
	while(i <= n) {
		int w,h, l;
		cin>>w>>h>>l;
		if (w <= 20 && h <= 20 && l <= 20) {
			cout<<"Case "<<i<<": "<<"good"<<endl;
		} else {
			cout<<"Case "<<i<<": "<<"bad"<<endl;
		}
		i++;
	}
	return 0;
}
