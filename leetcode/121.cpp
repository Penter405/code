#include <iostream>
#include <vector>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int before_lowest=prices[0],profit=0;
        for(int i=1;i<prices.size();i++){
            if(prices[i]-before_lowest>profit){
                profit=prices[i]-before_lowest;
            }
            if(prices[i]<before_lowest){
                before_lowest=prices[i];
            }
        }
        return profit;
    }
};