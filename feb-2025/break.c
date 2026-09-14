#include<stdio.h>
int main(){
    int num;
    for(;;){
        printf("For Exit ->please enter 0\n");
        printf("Enter a numbar :");
        scanf("%d",&num);
        if(num==0){
            printf("You exit from the loop:");
             break;
        }
        printf("num=%d\n",num);
    }
    return 0;
}