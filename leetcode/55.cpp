#include <vector>
class Solution {
public:
    bool canJump(std::vector<int>& nums) {
        int goal=nums.size()-1;
        if(goal==0){
            return true;
        }
        if(nums[0]==0){
            return false;
        }
        int last_reach=0,reachable=nums[0],reach_max=0;
        if(reachable>=goal){
            return true;
        }
        while(1){
            //std::cout<<"last_reach:"<<last_reach<<"   reachable:"<<reachable<<"  reach_max"<<reach_max<<"\n";
            
            for(int i=last_reach;i<reachable+1;++i){
                //std::cout<<"time:"<<i<<"\n";
                if(nums[i]==0){
                    //std::cout<<"index  '"<<i<<"' element = 0\n";
                    continue;
                }
                if(i>=goal){
                    return true;
                }
                if(i+nums[i]>reach_max){
                    //std::cout<<i<<"+"<<"index '"<<i<<"' element "<<nums[i]<<" is "<<i+nums[i]<<"\n";
                    reach_max=i+nums[i];
                }
            }
            if(reachable==reach_max){
                //std::cout<<"last max==now max, fuck up. end:reachable and reach_max is "<<reachable;
                return false;
            }
            last_reach=reachable;
            reachable=reach_max;
            if(reach_max>=goal){
                return true;
            }
        }
        return false;
    }
};