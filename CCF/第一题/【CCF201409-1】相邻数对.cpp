/*
	问题描述:
		给定n个不同的整数，问这些数中有多少对整数，它们的值正好相差1。

	输入格式:
		输入的第一行包含一个整数n，表示给定整数的个数。
　　	第二行包含所给定的n个整数。

	输出格式:
		输出一个整数，表示值正好相差1的数对的个数。

	样例输入:
		6
		10 2 6 3 7 8

	样例输出:
		3

	样例说明:
		值正好相差1的数对包括(2, 3), (6, 7), (7, 8)。

	评测用例规模与约定:
		1<=n<=1000，给定的整数为不超过10000的非负整数。
*/

#include <cstdio>
#include <algorithm>

using namespace std;

int str[1010];

int main(){
	
	int n;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		scanf("%d", &str[i]);
	}
	int sum=0;
	
	/*//此程序复杂度较高
	for(int i=0; i<n; i++){
		for(int j=i+1; j<n; j++){
			if(abs(str[i]-str[j]) == 1){
				sum++;
			}
		}
	}*/
	
	sort(str, str+n);
	
	for(int i=0; i<n-1; i++){
		if(str[i+1] - str[i] == 1){
			sum++;
		}
	}
	
	printf("%d", sum);
	
	return 0;
}





















