#include <iostream>
#include <string>
#include <unordered_map>
class Solution {
private:
    std::unordered_map<char,char> hash;
    
public:
    bool isPalindrome(std::string s) {
        auto front=s.begin();
        auto back=s.rbegin();
        for(;front!=s.end()&&back!=s.rend();){
            std::cout<<*front<<"  "<<*back<<"\n";
            while(*front==' '){
                if(++front==s.end()){
                    return true;
                }
            }
            while(*back==' '){
                if(++back==s.rend()){
                    return true;
                }
            }
            if(*front!=*back){
                return false;
            }
            ++front;
            ++back;
        }
        return true;
    }
};
//version 2
class Solution {
private:
    int word(char me){
        if((me>='A'&&me<='Z')||(me>='a'&&me<='z')||(me>='0'&&me<='9')){
            return 1;
        }
        return 0;
    }
    char lowwer(char me){
        if(me>'Z'&&(!(me>='0'&&me<='9'))){
            me-=32;
        }
        return me;
    }
    
public:
    bool isPalindrome(std::string s) {
        auto front=s.begin();
        auto back=s.rbegin();
        for(;front!=s.end()&&back!=s.rend();){
            
            while(!word(*front)){
                if(++front==s.end()){
                    return true;
                }
            }
            while(!word(*back)){
                if(++back==s.rend()){
                    return true;
                }
            }
            //std::cout<<*front<<"  "<<*back<<"\n";
            if(lowwer(*front)!=lowwer(*back)){
                return false;
            }
            ++front;
            ++back;
        }
        return true;
    }
};
/*

*/