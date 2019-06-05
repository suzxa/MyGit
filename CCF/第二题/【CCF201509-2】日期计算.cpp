/*
	问题描述:
		给定一个年份y和一个整数d，问这一年的第d天是几月几日？
	　　注意闰年的2月有29天。满足下面条件之一的是闰年：
	　　1） 年份是4的整数倍，而且不是100的整数倍；
	　　2） 年份是400的整数倍。

	输入格式:
	　　输入的第一行包含一个整数y，表示年份，年份在1900到2015之间（包含1900和2015）。
	　　输入的第二行包含一个整数d，d在1至365之间。

	输出格式:
	　　输出两行，每行一个整数，分别表示答案的月份和日期。

	样例输入:
		2015
		80

	样例输出:
		3
		21

	样例输入:
		2000
		40

	样例输出:
		2
		9
*/

#include <cstdio>

int month[12][2] = {{31, 31}, {28, 29}, {31, 31}, {30, 30}, {31, 31}, {30, 30}, {31, 31},
					{31, 31}, {30, 30}, {31, 31}, {30, 30}, {31, 31}};

bool isLeap(int a){
	if((a % 4 == 0 && a % 100 != 0) || a % 400 == 0){
		return true;
	}else{
		return false;
	}
}

int main(){
	
	int year, d;
	scanf("%d%d", &year, &d);
	int m=1, day=0;
	while(d--){
		day++;
		if(day == month[m-1][isLeap(year)] + 1){
			m++;
			day = 1;
		}
	}
	printf("%d\n%d", m, day);
	
	return 0;
}























