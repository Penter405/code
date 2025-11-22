#include <stdio.h>
int main(){
    printf("hi,Penter\n");
    int x;
    x=5;
    //printf("%i",x);
    printf("how many apple you want:\n");
    scanf("%i",&x);
    printf("you bought %i apple\nyou are going to pay us %i\n",x,x*5);
    printf("do you have enough money(Y or n):\n");
    char word[3];
    scanf(" %c",&word[0]);
    if(word[0]=='Y'){
        printf("thanks you,see you next time\n");
    }
    else{
        //char word2;
        printf("are you going to say sorry(Y or n):\n");
        scanf(" %c",&word[1]);
        if (word[1]=='Y'){
            printf("okay laaaa,99 dollar off\n");
            //char
            printf("are you sure not to buy with this discount(Y or n):\n");
            scanf(" %c",&word[2]);
            if (word[2]=='n'){
                printf("thanks for coming\n");
            }
            else if(word[2]=='Y'){
                printf("fuck off\n");
            }
        }
        else{
            printf("fuck off\n");
        }
        
    }

    
    return 0;
}