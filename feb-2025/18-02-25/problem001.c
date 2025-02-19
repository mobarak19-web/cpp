#include<stdio.h>
int main(){
    int i,a,b;
    printf("Enter the value of a:");
    scanf("%d",&a);
    printf("Enter the value of b:");
    scanf("%d",&b);
    i=a;
    while(i<=b){
        i++;
        if(i%2==0){
            printf("%d\t",i);
                
        }
       
    }
    return 0;
}