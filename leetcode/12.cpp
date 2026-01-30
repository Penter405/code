#include <iostream>
#include <unordered_map>
#include <array>
class Solution {
public:
    std::string intToRoman(int num) {
        std::string result;
        std::unordered_map<int,int> hash;
        std::array<int,13> coin={1000,900,500,400,100,90,50,40,10,9,5,4,1};
        std::array<std::string,13> word={"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        int time=0;
        for(int i=0;i<13;++i){
            time=num/coin[i];
            for(int p=0;p<time;++p){
                result+=word[i];
            }

            num-=time*coin[i];
        }
        return result;
    }
};