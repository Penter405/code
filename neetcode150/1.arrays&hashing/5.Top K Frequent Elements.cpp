/*
unordered_map , which is 無序,  but what is 有序 ,具體是什麼順序?
從小到大 , 從這個data type 就決定好的 不須用靠某個function 排序
也就是說 map 內建 從key 小到大 排序
*/


/*
++it vs it++
這是一個很有趣的記憶體問題

*/

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        #include <iostream>
        std:vector<int> result;
        std::map<int,int> hash;
        for(auto&it:nums){
            std::cout<<"hi";
            if(hash.find(it)!=hash.end()){
                hash[it]+=1;
            }else{
                hash[it]=1;
            }
        }
        int pointer=0;
        for(auto it=hash.rbegin();it<hash.rend() && pointer<k;it++)
        return result;
    }
};