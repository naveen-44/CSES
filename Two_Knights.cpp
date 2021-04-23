#include<bits/stdc++.h>
#define ll long long
using namespace std;
 
int main(){
	ll n;
	cin>>n;
	for(ll i = 1;i <= n; i++){
		ll a1 = i*i;
		ll x = (a1*(a1-1)/2);
		if(i>2){
			x-=4*(i-1)*(i-2);
		}
		cout<<x<<endl;
	}
}
