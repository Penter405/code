#include <iostream>
#include <unordered_map>
#include <string>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        if(s.size()!=t.size()){
            return 0;
        }
        std::unordered_map<char,int> sm, tm;
        for(int p=0;p<s.size();p++) {
            if(sm.find(s[p])!=sm.end()){
                sm[s[p]]+=1;
            }else{
                sm[s[p]]=1;
            }
        }
        for(int p=0;p<t.size();p++){
            if(sm.find(t[p])!=sm.end() && sm[t[p]]!=0){
                sm[t[p]]-=1;
            }else{
                return 0;
            }
        }
        return 1;
    }
};
