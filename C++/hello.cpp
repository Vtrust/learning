#include <stdio.h>
#include <math.h>
#include <string.h>
#define pi 3.14

void printArray(int a[],int n);
int main()
{
//	int a, b;
//	scanf("%d%d",&a,&b);
//	printf("%05d",a+b);
//	
//	char str2[25] = "Wo ai de ren bu ai wo";
//	printf("%s",str2);

//	int a = -10;
//	printf("%f\n%f",fabs(a),pi);
	
//	int a[5][6]={{3,2,1},{1,2,3},{},{5,3,2,1}};
//	for(int i = 0;i<5;i++){
//		for(int j=0;j<6;j++){
//			printf("%d",a[i][j]);
//		}
//		printf("\n");
//	}

//  memset
//	int a[5] = {1,2,3,4,5};
//	memset(a,1,sizeof(a));
//	//printf("%d %d",sizeof(a),sizeof(a[0]));
//	printArray(a,5);

//string¸³Öµ
//	char str[3][3];
//	for(int i = 0;i<3;i++){
//		for(int j = 0;j<3;j++){
//			str[i][j]=getchar();
//		}
//		getchar();
//	}
//	
//	printf("%s",str); 
	
//	char str1[15];
//	for(int i = 0;i<5;i++){
//		str1[i]=getchar();
//	}
//	puts(str1);
//	
//	printf("%d",strlen(str1));

//	sscanf sprintf
	int n;
	double db;
	char str[100] = "2048:3.14,hello", str2[100];
	sscanf(str,"%d:%lf,%s",&n,&db,str2);
	printf("n=%d,db=%.2f,str2=%s\n",n,db,str2); 
	
	return 0;
}

void printArray(int a[],int n){
	for(int i=0;i<n;i++){
		printf("%d ",a[i]);
	}
}
