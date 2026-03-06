#include <string>
#include <iostream>
using namespace std;
class Solution {
public:
    bool checkOnesSegment(string s) {
        int seem_0=0;
        for(auto& it:s){
            if(it=='0'){
                seem_0=1;
                continue;
            }
            if(it && seem_0){
                return false;
            }

        }
        return true;
    }
};