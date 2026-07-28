//20 to 30 minute costed
#include <bits/stdc++.h>
using namespace std;
class Solution {
private:
    bool is_letter(char x){
        if(x-'a'>=0 && x-'a'<=25){
            return true;
        }
        if(x-'A'>=0 && x-'A'<=25){
            return true;
        }
        if(x-'0'>=0 && x-'0'<=9){
            return true;
        }
        return false;
    }
    char to_small(char x){
        //std::cout<<"origin "<<x;
        if(x-'A'>=0 && x-'A'<=25){
            //std::cout<<"get it "<<char('a'+x-'A')<<'\n';
            return char('a'+x-'A');
        }
        return x;
    }
public:
    bool isPalindrome(string s) {
        //std::cout<<'Z'-'A';
        //std::cout<<char('?');
        auto front=s.begin();
        auto back=s.rbegin();
        for(int x=0;x<(s.size()/2);x++){
            //std::cout<<*front<<' '<<*back<<'\n';
            if((front)==s.end() || (back)==s.rend()){
                return true;
            }
            while(is_letter(*front)==false){
                if(front==s.end()){
                    return true;
                }
                front++;
            }
            while(is_letter(*back)==false){
                if(back==s.rend()){
                    return true;
                }
                back++;
            }
            if(to_small((*front))!=to_small((*back))){
                return false;
            }
            front++;
            back++;
        }
        return true;
    }
};
