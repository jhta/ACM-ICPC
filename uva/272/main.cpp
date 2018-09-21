#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	string s;
	bool f = true;
	while(getline(cin, s)) {
	 
	 for (int i = 0; i < s.length(); i++) {
	   if (s[i] == 34) {
		if (f) {
			f = false;
			s[i] = 96;
			s.insert(i, "`");
		} else {
			f = true;
			s[i] = 39;
			s.insert(i, "'");
		}
	   }
	 }
	 cout<<s<<endl;
	}
	
	return 0;
}
