#include <bits/stdc++.h>
using namespace std;
class Solution {
private:
    std::unordered_map<char,char> partner;
    
public:
    bool isValid(string s) {
        //partner['(']=')';
        partner[')']='(';
        //partner['[']=']';
        partner[']']='[';
        //partner['{']='}';
        partner['}']='{';
        std::vector<char> buffer;
        for(auto& it:s){
			if(buffer.empty() || buffer.back()!=partner[it]){
                buffer.push_back(it);
            }else{
                buffer.pop_back();
            }
        }
        return buffer.size()==0;
    }
};
