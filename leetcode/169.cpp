#include <vector>
#include <map>
#include <iostream>
class Solution {
public:
    int majorityElement(std::vector<int>& nums) {
        int big_guy,big_num=0;
        std::map<int,int> hash;//map :o(log n) findding, its binary tree ////unordered_map 0(1), seldom o(n)
        for(auto&it:nums){
            if(hash.find(it)!=hash.end()){
                hash[it]+=1;
                    
            }else{
                hash[it]=1;
            }
            if(hash[it]>big_num){
                big_guy=it;
                big_num=hash[it];
            }
        
        }
        return big_guy;
        
        
    }
};