#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    std::vector<int> dp;
    int max(int a,int b){
        if(a>b){
            return a;
        }
        return b;
    }

    int get(int want){
        if(want<0){
            return 0;
        }
        return dp[want];
    }
    int rob(vector<int>& nums) {
        for(int i=0;i<nums.size();++i){
            dp.push_back(max(nums[i]+get(i-2),get(i-1)));
        }
        return dp.back();
    }
};