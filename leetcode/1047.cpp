#include <bits/stdc++.h>
class Solution {
public:
    string removeDuplicates(string s) {
        std::vector<char> stack;
        for(auto& it:s){
            if(stack.empty()){
                stack.push_back(it);
                continue;
            }
            if(stack.back()==it){
                continue;
            }
            stack.push_back(it);
        }
        //std::string result;
        //result=to_string();
        return to_string(stack);
    }
};