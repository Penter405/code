#include <iostream>
#include <vector>
#include <unordered_map>
class Solution {
public:
    bool hasDuplicate(std::vector<int>& nums) {
        bool yesno=0;
        int size;
        std::unordered_map<int,int> hash;
        size=nums.size();
        for(int i=0;i<size;i++){
            std::cout<<"run"<<" times, now:"<<i<<"\n";
            if(hash.find(nums[i])!=hash.end()){
                std::cout<<"find";
                yesno=1;
                return yesno;
            }else{
                hash[nums[i]]=1;
            }
        }
        return yesno;
    }
};