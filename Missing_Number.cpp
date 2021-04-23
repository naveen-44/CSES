#include <bits/stdc++.h>
using namespace std;
#define ll long long
 
int main(){
	ll n,s=0;
	ll x;
	cin>>n;
	for(int i = 1;i<n;i++){
		cin>>x;
		s+=x;
	}
	cout<<(n*(n+1)/2)-s;
	return 0;
}
