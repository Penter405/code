#include <iostream>
#include <unordered_map>
class Solution {
private:
    std::unordered_map<int,int> hash_dp{{0,0},{1,1}};
public:
    int fib(int n) {
        //my first c++ recursion, we need debug cout;
        std::cout<<"soving n is <"<<n<<">\n";
        if(hash_dp.find(n)!=hash_dp.end()){
            std::cout<<"find "<<n<<" is in hashtable. return "<<hash_dp[n]<<"\n";
            return hash_dp[n];
        }
        //make it in hash_dp
        //because return in if(), we don need else{}
        std::cout<<"bad news: element "<<n<<" is not in hashtable\n";
        int ans=fib(n-1)+fib(n-2);
        std::cout<<"adding element "<<n<<" to hashtable. the vaule is "<<ans<<"\n";
        hash_dp[n]=ans;
        return ans;
    }
};