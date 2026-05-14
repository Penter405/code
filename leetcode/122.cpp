class Solution {
public:
    int maxProfit(vector<int>& prices) {
        //int is_yesterday_happy=0;
        //int is_bought=0;
        int profit=0;
        int bought_price=prices.front();
        int last=prices.front();
        for(int i=0;i<prices.size();++i){
            if(last>(prices[i])){
                profit+=last-bought_price;
                bought_price=prices[i];
            }
            last=prices[i];
        }
        profit+=last-bought_price;
        return profit;
    }
};