#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int countPrimes(int n) {
        int result=0;
        std::vector<int> is_prime(n,1);
        /*for(auto&it:is_prime){
            std::cout<<it<<"\n";
        }
        */
        if(n==0||n==1){
            return 0;
        }
        is_prime[0]=0;//we dont use 0 element
        is_prime[1]=0;//int 1 wont be prime
        for(int i=1;i<n;++i){
            if(is_prime[i]){
                //std::cout<<"int "<<i<<"is prime\n";
                ++result;
                for(int pe=i+i;pe<n;pe+=i){
                    is_prime[pe]=0;
                }
            }
        }
        return result;
    }
};