#include<vector>
using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        
        //array bigger or equal to target
        //right pointer in the second of array
        //but it could be no result or result 1 or size of array.
        auto right=nums.begin(),left=nums.begin();
        int result=nums.size()+1,sum=nums[0],size=1;
        for(;;){
            if(sum>=target && size<result){
                result=size;
            }
            if(sum>target){
                sum-=*(left++);
                --size;
            }else{
                if(++right!=nums.end()){
                    sum+=*right;
                    ++size;
                }else{
                    break;
                }
                
            }
        }
        if(result==nums.size()+1){
            return 0;
        }
        return result;
    }
};