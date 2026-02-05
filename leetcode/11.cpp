//it is some version in python ide
#include <vector>
#include <iostream>
class Solution {
private:
    int min(int a,int b){
        if(a<b){
            return a;
        }
        return b;
    }
public:
    int maxArea(std::vector<int>& height) {
        auto front=height.begin();
        auto back=height.rbegin();
        int big=-1;
        int len=height.size()-1;
        for(;len!=0;){
            
            if(len*min(*front,*back)>big){
                big=len*min(*front,*back);
            }
            //std::cout<<len<<" * "<<min(*front,*back)<<" == "<<big<<'\n';
            if(*front<*back){
                front++;
            }else{
                back++;
            }

            len--;
        }
        return big;
    }
};