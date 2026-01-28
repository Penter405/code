/*
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int i=0;
        std::vector<int> result_bot,result;
        std::set<int> hash;//banned index of nums
        if (k>nums.size()){
            k=nums.size();
        }
        while(i<k){
            int big_index=-1,big_integer;
            for(int inner_i=0;inner_i<nums.size();inner_i++){
                if(hash.find(inner_i)==hash.end() && (big_index==-1 || nums[inner_i]>big_integer)){
                    big_integer=nums[inner_i];
                    big_index=inner_i;
                }
            }
            //nums[big_index]=-1; there are negative element, cant use
            if(big_index!=-1){
                hash.insert(big_index);
                result_bot.push_back(big_integer);
            }
            

            i++;
        }
        
        //k* nums.size()*log n+k+nums.size *log n
        // or we can do erase with k* nums.size()[less every time]*nums.size()[less every time]+nums.size
        for(int inner_i=k-1;inner_i>=0;inner_i--){
            result.push_back(result_bot[inner_i]);
        }
        for(int inner_i=0;inner_i<nums.size();inner_i++){
            if(hash.find(inner_i)==hash.end()){
                result.push_back(nums[inner_i]);
            }
            
        }

        for(auto&it:result_bot){
            cout<<it<<",";
        }
        nums=result;
    }
};
*/

//these is wrong. in fact, we need to rotate.
#include <vector>
#include <iostream>
class Solution {
public:
    void rotate(std::vector<int>& nums, int k) {
        
        k=k%nums.size();
        std::vector<int> result;
        if(k!=0){
            for(int i=nums.size()-k;i<nums.size();i++){
                result.push_back(nums[i]);
            }
            for(int i=0;i<nums.size()-k;i++){
                result.push_back(nums[i]);
            }
            nums=result;
        }
    }
};