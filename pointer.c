#include <stdio.h>
#include <stdlib.h>
int* pen(){
    int* x=(int*)malloc(5*sizeof(int));
    for(int counter=0,value=0;counter<5;counter++,value++){
        x[counter]=value;
    }
    //*x=5;
    return x;
}
int main(){
    {
    int* p;
    p=pen();
    for(int i=0;i<5;i++){
        printf("%i\n",p[i]);
    }
    //print("%i",p[0]);
    free(p);
    }
    char chinese_name[]="有";
    printf("%zu",sizeof(chinese_name));
    printf("%s",chinese_name);

    return 0;
}