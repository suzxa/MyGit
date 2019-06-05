/*
	问题描述:
		小明的公司每个月给小明发工资，而小明拿到的工资为交完个人所得税之后的工资。假设他一个月的税前工
	资（扣除五险一金后、未扣税前的工资）为S元，则他应交的个人所得税按如下公式计算：
	　　1）个人所得税起征点为3500元，若S不超过3500，则不交税，3500元以上的部分才计算个人所得税，令A=S-3500元；
	　　2）A中不超过1500元的部分，税率3%；
	　　3）A中超过1500元未超过4500元的部分，税率10%；
	　　4）A中超过4500元未超过9000元的部分，税率20%；
	　　5）A中超过9000元未超过35000元的部分，税率25%；
	　　6）A中超过35000元未超过55000元的部分，税率30%；
	　　7）A中超过55000元未超过80000元的部分，税率35%；
	　　8）A中超过80000元的部分，税率45%；
	　　例如，如果小明的税前工资为10000元，则A=10000-3500=6500元，其中不超过1500元部分应缴税1500×3%=45元，
	超过1500元不超过4500元部分应缴税(4500-1500)×10%=300元，超过4500元部分应缴税(6500-4500)×20%=400元。总
	共缴税745元，税后所得为9255元。
	　　已知小明这个月税后所得为T元，请问他的税前工资S是多少元。

	输入格式:
		输入的第一行包含一个整数T，表示小明的税后所得。所有评测数据保证小明的税前工资为一个整百的数。

	输出格式:
		输出一个整数S，表示小明的税前工资。

	样例输入:
		9255

	样例输出:
		10000

	评测用例规模与约定:
		对于所有评测用例，1 ≤T ≤100000。
*/

#include <cstdio>

//以下所有对应金额都先减去了3500
const int base = 3500;
const double max_rate = 0.45;
const int wage_pre[6] = {1500, 4500, 9000, 35000, 55000, 80000};//对应当前税率的最大的A
const int wage_aft[6] = {1455, 4155, 7755, 27255, 41255, 57505};//对应最大A的税后金额
const double tax_rate[6] = {0.03, 0.1, 0.2, 0.25, 0.3, 0.35};

//这里有一个重要的公式：A - (A-wage_pre[i]) * tax_rate[i+1] - 后面区间的税费(都是固定的) = t
//                      wage_pre[i] - 后面区间的税费(都是固定的) = wage_aft[i]
//综合以上公式可以得到：A = (t-wage_aft[i]) / (1-tax_rate[i+1]) + wage_pre[i]!!!!!
int main(){
	
	int n;
	scanf("%d", &n);
	int t = n-base;//t对应A的税后金额
	int A = 0;
	if(t < 0){
		A = t;
	}else if(t > wage_aft[5]){
		A = (t-wage_aft[5]) / (1-max_rate) + wage_pre[5];
	}else{
		int i;
		for(i=0; i<6; i++){
			if(t < wage_aft[i]){
				break;
			}
		}
		if(i == 0){//特殊情况，即A要小于1500，无法用公式求得
			A = t / (1-tax_rate[i]);
		}else{
			A = (t-wage_aft[i-1]) / (1-tax_rate[i]) + wage_pre[i-1];
		}
	}
	printf("%d", A+base);
	
	return 0;
}





















