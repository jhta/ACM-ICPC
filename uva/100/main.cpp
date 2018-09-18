#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
	// your code goes here
	int i, j;
	while(scanf ("%d %d", &i, &j) != EOF) {
		int print_i = i, print_j = j;
		//cout<<i<<" "<<j<<endl;
		if (i > j) swap(i, j);
		int max_cycle = 0;
		while(i <= j) {
			//cout<<j<<endl;
			int cycle = 1;
			int n = j;
			while(n > 1) {
				if (n % 2 == 1) n = (3 * n) + 1;
				else n = n / 2;
				cycle++;
				//cout<<"n: "<<n<<endl;
			}
			max_cycle = max(max_cycle, cycle);
			j--;
		}
		cout<<print_i<<" "<<print_j<<" "<<max_cycle<<endl;
		
	}
	
	return 0;
}
