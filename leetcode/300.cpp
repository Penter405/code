//did not finish

#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> dp;
    map<int,int> sorted;//key=total; value=minimum number in that total
    int lengthOfLIS(vector<int>& nums) {
        for(int i =0;i<nums.size();++i){
            int now_beat_child_length=0;
            for(auto child:sorted){
                
                cout<<child.first<<"  "<<child.second;
                if(child.first>now_beat_child_length && child.second){
                    return 0;
                }
            }
            dp.push_back(1+now_beat_child_length);
        }
        for(auto it:dp){
            cout<<it;
        }
        int best=dp[0];
        for(auto it:dp){
            if(it>best){
                best=it;
            }
        }
        return best;
    }
};

Solution Penter=Solution();
int main(){
    vector<int> data={10,9,2,5,3,7,101,18};
    Penter.lengthOfLIS(data);
    return 0;
}