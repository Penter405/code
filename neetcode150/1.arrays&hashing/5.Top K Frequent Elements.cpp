/*
unordered_map , which is 無序,  but what is 有序 ,具體是什麼順序?
從小到大 , 從這個data type 就決定好的 不須用靠某個function 排序
也就是說 map 內建 從key 小到大 排序
*/


/*
++it vs it++
這是一個很有趣的記憶體問題

*/
#include <vector>
#include <map>
class Solution {
public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        #include <iostream>
        std::vector<int> result;
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

//26y 1m28d version below
class Solution {
private:
    find_place(multi,b,index){
        //find index the b should go into 'multi' array 
        //insert after the 'index',return the iterator bacause the insert needs iterator but not index.
        //sure he is the small showing
        int last,index=-1;
        auto it=multi.begin();
        auto last_it=multi.before_begin();
        for(;it!=multi.end();){
            index+=1
            if(it==multi.begin()){
                last=it->second;
                continue;
            }else if(last>b){
                return last_it
            }else if(last<b && b<(it->second)){
                return last_it;
            }
            last=it->second;
            last_it=it++;
        }
        return last_it;
    }
    void add_two(inner_result,inner_time,target_a,target_b){
        //from b showen place insert, using forword_list, its a single link vector k*k
        //not doing this,k*k*k,for loop & find place to insert,we do need to know place by o(n) seeing & insert
        //for loop & push_back() & find smallest& remove k*k, this would be better
        //basely, insert is the key
        int size;
        auto iter=find_place(inner_time,target_b,size);
        inner_time.insert_after(iter,target_b);
        int i=0;
        for(auto it=inner_result.before_begin();it!=inner_result.end();){
            if(size==i){
                inner_result.insert_after(it,target_a);
                break;
            }
            ++i;
        }
        

    }
public:
    vector<int> topKFrequent(std::ector<int>& nums, int k) {
        //#include <iostream>
        //#include <forward_list>
        std::forward_list<int,k> result,time;
        std::map<int,int> hash;
        for(auto&it:nums){
            std::cout<<"hi";
            if(hash.find(it)!=hash.end()){
                hash[it]+=1;
            }else{
                hash[it]=1;
            }
        }
        int pointer=0,size=0,small;
        for(auto it=hash.begin();it<hash.end() && pointer<k;it++){
            if(size=0){
                bot_small=time.before_begin();
                time.insert(bot_small,it);
                bot_result=result.before_begin();
                result.insert(bot_result,it)
                ++size
            }else{
                /*if((it->second)<small){
                    bot_small=time.begin();
                    *bot_small=it->second;
                }else{
                */
                add_two()
                if(size==k){
                    result.pop_front();
                    time.pop_front();
                }else{
                    ++size;
                }
            }
        
            
        
        return result;
    
    }
    }
    
};