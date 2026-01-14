#include <iostream>
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::vector<int> answer;
        std::unordered_map<int,int> hash;
        int size=nums.size();
        for(int p=0;p<size;p++){
            if(hash.find(nums[p])!=hash.end()){
                answer.push_back(hash[nums[p]]);
                answer.push_back(p);
            }else{
                hash[target-nums[p]]=p;
            }
            
        }
    return answer;
    }
    
};
