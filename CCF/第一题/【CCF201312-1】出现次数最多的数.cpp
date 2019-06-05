/*
	问题描述:
		给定n个正整数，找出它们中出现次数最多的数。如果这样的数有多个，请输出其中最小的一个。

	输入格式:
	　　输入的第一行只有一个正整数n(1 ≤ n ≤ 1000)，表示数字的个数。
	　　输入的第二行有n个整数s1, s2, …, sn(1 ≤ si≤ 10000, 1 ≤ i ≤ n)。相邻的数用空格分隔。

	输出格式:
	　　输出这n个次数中出现次数最多的数。如果这样的数有多个，输出其中最小的一个。

	样例输入:
		6
		10 1 10 20 30 20

	样例输出:
		10
*/

#include <cstdio>
#include <algorithm>

using namespace std;

int str[10010];

int main(){
	
	int n, m;
	int max_num=0;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		scanf("%d", &m);
		str[m]++;
		max_num = max(max_num, m);//方便确定上限，减少循环次数
	}
	int k=0;
	for(int i=0; i<=max_num; i++){
		if(str[k] < str[i]){//用大于号在于确保输出次数最多的数最小
			k = i;
		}
	}
	
	printf("%d", k);
	
	return 0;
}


















