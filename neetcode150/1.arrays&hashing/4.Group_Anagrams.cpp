#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>
class Solution {
public:
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        std::vector<std::vector<std::string>> result;
        std::unordered_map<std::unordered_set<std::string>,int> hash;
        short int index=0;//2^10 is okay, im not sure wheather short is enough or not. said question:"1 <= strs.length <= 1000."
        //set is hashable
        //dict[set]
        for(int p=0;p<strs.size();p++){
            if(hash.find(strs[p])!=hash.end()){
                result[hash[strs[p]]].push_back(strs[p]);
            }else{
                hash.insert(strs[p])=index;
                std::vector<string> bot;
                bot.insert(strs[p]);
                result.insert(bot);
                index++;
            }
        }
        return result;
    }
};
/*
cpp is a strong data type language
the "no changing data type" rule include inner data
in this solution, i initial hash variable as unordered_map, and the inner data type is 
key: unordered_set<string>
value:int
but in some run like row 18, i add a key with string only.
*/