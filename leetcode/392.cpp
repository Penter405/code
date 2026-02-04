#include <string>
class Solution {
public:
    bool isSubsequence(std::string s, std::string t) {
        auto sub=s.begin();
        auto origin=t.begin();
        for(;;){
            if(origin==t.end()){
                if(sub==s.end()){
                    return true;
                }
                return false;
            }
            if(*sub==*origin){
                ++sub;
                ++origin;
            }else{
                ++origin;
            }
        }
    }
};