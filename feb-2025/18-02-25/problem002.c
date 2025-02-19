  #include<stdio.h>
int main(){
   int i,a,b;
    printf("Enter the value of a:");
    scanf("%d",&a);
    printf("Enter the value of b:");
    scanf("%d",&b);
    for(i=a;i<b;i+=2){
        if(i%2==1){
            printf("%d  ",i);
        }
    }
    return 0;
}