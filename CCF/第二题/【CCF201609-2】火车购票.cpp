/*
	问题描述:
		请实现一个铁路购票系统的简单座位分配算法，来处理一节车厢的座位分配。
	　　假设一节车厢有20排、每一排5个座位。为方便起见，我们用1到100来给所有的座位编号，第一排是1到5号，
	第二排是6到10号，依次类推，第20排是96到100号。
	　　购票时，一个人可能购一张或多张票，最多不超过5张。如果这几张票可以安排在同一排编号相邻的座位，则
	应该安排在编号最小的相邻座位。否则应该安排在编号最小的几个空座位中（不考虑是否相邻）。
	　　假设初始时车票全部未被购买，现在给了一些购票指令，请你处理这些指令。

	输入格式:
		输入的第一行包含一个整数n，表示购票指令的数量。
	　　第二行包含n个整数，每个整数p在1到5之间，表示要购入的票数，相邻的两个数之间使用一个空格分隔。

	输出格式:
		输出n行，每行对应一条指令的处理结果。
　　	对于购票指令p，输出p张车票的编号，按从小到大排序。

	样例输入:
		4
		2 5 4 2

	样例输出:
		1 2
		6 7 8 9 10
		11 12 13 14
		3 4

	样例说明:
		1) 购2张票，得到座位1、2。
	　　2) 购5张票，得到座位6至10。
	　　3) 购4张票，得到座位11至14。
	　　4) 购2张票，得到座位3、4。

	评测用例规模与约定:
		对于所有评测用例，1 ≤n ≤100，所有购票数量之和不超过100。
*/

#include <cstdio>

int T[101];//记录100个座位是否为空

int main(){
	
	int n, m;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		scanf("%d", &m);
		bool flag = false;//标记，为了判断是否坐在一排。没有，则按最小序号散坐
		
		for(int j=1; j<=20 && (!flag); j++){//从每一排开始判断是否能在一排坐下m个人
			int cnt=0;//计数
			for(int k=1; k<=5; k++){
				int pos = (j-1)*5+k;//将行列转换为序号
				if(T[pos] == 0){//座位空着，人数加1
					cnt++;
				}else{
					cnt = 0;
				}
				if(cnt == m){//一排满足要求，可以坐m个人
					for(int t=pos-m+1; t<=pos; t++){
						printf("%d ", t);
						T[t] = 1;//标记座位不为空
					}
					flag = true;//一个人的购票座位安排完毕，进行下一个人的
					break;
				}
			}
		}
		
		if(!flag){//任一一排不能安排坐在一排，则按序散坐
			int cnt=0;
			for(int j=1; j<=100; j++){
                if(T[j] == 0){
					T[j] = 1;
					cnt++;
					printf("%d ", j);
				}
				if(cnt == m){
					break;
				}
			}
		}
		
		printf("\n");
	}
	
	return 0;
}























