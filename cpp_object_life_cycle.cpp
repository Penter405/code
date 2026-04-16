#include <iostream>
int* a;
int doing(){
        int b=5;
        a=&b;
        return 0;//variable b deleted, any try to use its data is undefined behavior
    }
int main(){
    doing();
    std::cout<<*a;//we try to use it, but its ub, the c++ dont promis

}
