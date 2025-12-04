#include <stdio.h>
#include <stdlib.h>
int* array_of_int_pointer(){
    int* x=(int*)malloc(5*sizeof(int));
    for(int counter=0,value=0;counter<5;counter++,value++){
        x[counter]=value;
    }
    //*x=5;
    return x;
}
void output_array_of_int_malloc(){
    int* p;
    p=array_of_int_pointer();
    for(int i=0;i<5;i++){
        printf("%i\n",p[i]);
    }
    //print("%i",p[0]);
    free(p);
}
FILE* read_data(){
    FILE *p=fopen("/workspaces/code/data.txt","r");
    FILE *rp=p;
    if (!p) {
        printf("無法開啟檔案\n");
        return rp;
    }
    printf("%zu\n",sizeof(p));
    char buffer[512];
    int counter=0;
    int doing=1;
    int right_row_end[3];
    while (fgets(buffer, 512, p)) {
        counter++;
        printf("%s", buffer);
        printf("done %i\n",counter);
    }
    return rp;
}
int* data_get_per_question_start_and_end_row(){
    FILE *p=fopen("/workspaces/code/data.txt","r");

}
void output_chinese_character(){
    char chinese_name[]="有";
    printf("%zu\n",sizeof(chinese_name));
    printf("%s\n",chinese_name);
}
int search(char* what){
    int size;
    
    switch what{
        
    }
}
int main(){
    output_array_of_int_malloc();
    output_chinese_character();
    read_data();



    return 0;
}