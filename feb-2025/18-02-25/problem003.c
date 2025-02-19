#include <stdio.h>

int main() {
    int a,b,i;
     printf("Enter the  value of a:");
   scanf("%d",&a);
    printf("Enter the  value of b:");
    scanf("%d",&b);
    for(i=a;i<=b; i+=2){
        if(b%2==0){
            printf("%d ",i);
    
        }

        
        }
       
    return 0;
}
