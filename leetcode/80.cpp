class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        //two pointer
        int be=0;
        int repeat=1;
        for(int see=1;see<nums.size();++see){
            std::cout<<see<<"   "<<be<<"  "<<nums[see]<<"  "<<nums[be]<<"  "<<repeat<<"\n";
            if(nums[see]==nums[be]){
                if(repeat==2){
                    continue;
                }
                ++repeat;
            }else{
                repeat=1;
            }
            ++be;
            std::cout<<"add\n";
            nums[be]=nums[see];
        }
        nums.resize(be+1);
        for(auto it:nums){
            std::cout<<it<<"  ";
        }
        return be+1;
    }
};