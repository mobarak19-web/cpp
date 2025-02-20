#include<stdio.h>
int main(){
    int i,a,b;
    printf("Enter the value of a:");
    scanf("%d",&a);
    printf("Enter the value of b:");
    scanf("%d",&b);
    
    i=a;
    printf("All positive numbar are: ");
    while(i<=b){
        
        if(i%2==0){
            printf("%d, ",i);
                
        }
       i++;
    }
    
    return 0;
}
