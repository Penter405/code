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
#include <forward_list>
#include <iostream>
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
    auto find_place(std::forward_list<int>& multi, int b, int& index){
        //find index the b should go into 'multi' array 
        //insert after the 'index',return the iterator bacause the insert needs iterator but not index.
        //sure he is the small showing
        int last,index=-1;
        auto it=multi.begin();
        auto last_it=multi.before_begin();
        for(;it!=multi.end();){
            index+=1;
            if(it==multi.begin()){
                last=*it;
                continue;
            }else if(last>b){
                return last_it;
            }else if(last<b && b<(*it)){
                return last_it;
            }
            last=*it;
            last_it=it++;
        }
        return last_it;
    }
    void add_two(std::forward_list<int>& inner_result, std::forward_list<int>& inner_time, int target_a, int target_b){
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
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        //#include <iostream>
        //#include <forward_list>
        std::forward_list<int> result,time;
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
        for(auto it=hash.begin();it!=hash.end() && pointer<k;it++){
            if(size==0){
                auto bot_small=time.before_begin();
                time.insert_after(bot_small,it->second);
                auto bot_result=result.before_begin();
                result.insert_after(bot_result,it->first);
                ++size;
            }else{
                /*if((it->second)<small){
                    bot_small=time.begin();
                    *bot_small=it->second;
                }else{
                */
                add_two(result,time,it->first,it->second);
                if(size==k){
                    result.pop_front();
                    time.pop_front();
                }else{
                    ++size;
                }
            }
        std::vector<int> final_result;
        for(auto it=time.begin();it!=time.end();++it){
            final_result.push_back(*it);
        }

        return final_result;
    
    }
    }
    
};
//2026/1/29 version below
#include <iostream>
#include <vector>
#include <forward_list>
class Solution {
private:
    auto find_place(std::forward_list<int>& multi, int b, int& index){
        //find index the b should go into 'multi' array 
        //insert after the 'index',return the iterator bacause the insert needs iterator but not index.
        //sure he is the small showing
        int last;
        index=-1;
        auto it=multi.begin();
        auto last_it=multi.before_begin();
        for(;it!=multi.end();){
            
            if(it==multi.begin()&&b<=(*it)){
                if(b<=(*it)){
                    return last_it;
                }
                
                //last=*it;
                //continue;
            }else if(last<=b && b<(*it)){
                return last_it;
                //std::cout<<last<<"\n";
            }
            index+=1;
            last=*it;
            last_it=it++;
        }
        return last_it;
    }
    void add_two(std::forward_list<int>& inner_result, std::forward_list<int>& inner_time, int target_a, int target_b){
        //from b showen place insert, using forword_list, its a single link vector k*k
        //not doing this,k*k*k,for loop & find place to insert,we do need to know place by o(n) seeing & insert
        //for loop & push_back() & find smallest& remove k*k, this would be better
        //basely, insert is the key
        int inner_size;
        auto iter=find_place(inner_time,target_b,inner_size);
        //std::cout<<"  inner_size"<<inner_size;
        inner_time.insert_after(iter,target_b);
        int i=-1;
        for(auto it=inner_result.before_begin();it!=inner_result.end();){
            if(inner_size==i){
                inner_result.insert_after(it,target_a);
                break;
            }
            ++i;
            ++it;
        }
        

    }
public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        std::forward_list<int> result,time;
        std::map<int,int> hash;
        for(auto&it:nums){
            //std::cout<<"hi";
            if(hash.find(it)!=hash.end()){
                hash[it]+=1;
            }else{
                hash[it]=1;
            }
        }
        //for(auto it=hash.begin();it!=hash.end();it++){
            //std::cout<<"key:"<<it->first<<"  value:"<<it->second<<"\n";
        //}


        int pointer=0,size=0,small;
        for(auto it=hash.begin();it!=hash.end() && pointer<k;it++){
            //std::cout<<"size"<<size;
            if(size==0){
                auto bot_small=time.before_begin();
                time.insert_after(bot_small,it->second);
                auto bot_result=result.before_begin();
                result.insert_after(bot_result,it->first);
                ++size;
            }else{
                /*if((it->second)<small){
                    bot_small=time.begin();
                    *bot_small=it->second;
                }else{
                */
                add_two(result,time,it->first,it->second);
                if(size==k){
                    result.pop_front();
                    time.pop_front();
                }else{
                    ++size;
                }
            }
            //cout<<"   result";
            //for(auto&hi:result){
                //std::cout<<hi;
            //}
            //cout<<"   time";
            //for(auto&hi:time){
               //std::cout<<hi;
            //}
            //std::cout<<"\n";
        }
        //std::cout<<"\n";
        //for(auto&it:result){
            //std::cout<<it;
        //}
        //std::cout<<"\n";
        //for(auto&it:time){
            //std::cout<<it;
        //}
        std::vector<int> final_result;
        for(auto it=result.begin();it!=result.end();++it){
            final_result.push_back(*it);
        }

        return final_result;
    
    
    }
    
};
//2026/1/29 version two below
#include <iostream>
#include <vector>
#include <forward_list>
#include <unordered_map>
class Solution {
public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        std::vector<int> result;
        std::unordered_map<int,int> hash;
        for(auto&it:nums){
            if(hash.find(it)!=hash.end()){
                hash[it]+=1;
            }else{
                hash[it]=1;
            }
        }
        int bigest,guy;
        auto iter=hash.begin();
        for(int i=0;i<k;++i){
            if(hash.begin()==hash.end()){
                break;
            }
            bigest=0,guy=0;
            auto it=hash.begin();
            for(;it!=hash.end();){
                if(it->second>bigest){
                    bigest=it->second;
                    guy=it->first;
                    iter=it;
                }
                ++it;

            }
            hash.erase(iter);
            result.push_back(guy);
        }
        return result;
    
    
    }
};
