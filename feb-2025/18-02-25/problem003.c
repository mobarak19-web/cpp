#include <stdio.h>

int main() {
    int a,b,i;
     printf("Enter the  value of a:");
   scanf("%d",&a);
    printf("Enter the  value of b:");
    scanf("%d",&b);
    printf("All divisor of a is: ");
    for(i=1;i<=b; i++){
        if(i%a==0){
            printf("%d, ",i);
    
        }

        
        }
       
    return 0;
}
