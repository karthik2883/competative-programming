/*
 Time complexity (without Dp):O(2^n)
 Time complexity (without Dp):O(2^n)

*/
#include<bits/stdc++.h>
using namespace std;

class fib
{
	int n,a,b,c;
public:
	void fibonacci() {
		a = 0; b=1;
		cout<< "Enter number of terms";
		cin>>n;
		for (int i=1; i<=n; i++) {
			cout<<a<<endl;
			c=a+b;
			a=b;
			b=c;
		}
	}
	//~fib();
	
};

int main() {
	fib f;
	f.fibonacci();

   return 0;

}