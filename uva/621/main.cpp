#include <bits/stdc++.h>
using namespace std;

int main() {
	
	regex r(".*35$");
	regex r1("^190.*");
	regex r3("^9.*4$");
	
	
	int n, i = 1;
	cin>>n;
	while(n--) {
		string s;
		cin>>s;
		if (s == "1" || s == "4" || s == "78" ) {
			cout<<"+"<<endl;
		} else if (regex_match(s, r)) {
			cout<<"-"<<endl;
		} else if (regex_match(s, r1)) {
			cout<<"?"<<endl;
		} else if (regex_match(s, r3)) {
			cout<<"*"<<endl;
		} else {
			cout<<"+"<<endl;
		}
		
	}
	return 0;
}
