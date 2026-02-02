#include <iostream>
#include <string>

class Solution {
public:
    int lengthOfLastWord(std::string s) {
        //There will be at least one word in s.
        int result=0;
        for(auto pointer=s.rbegin();pointer<s.rend();++pointer){
            std::cout<<*pointer;
            if(*pointer!=' '){
                ++result;
            }else{
                if(result!=0){
                    return result;
                }
                
            }
            
        }
        return result;
    }
};