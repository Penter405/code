#include <bits/stdc++.h>
class Solution {
private:
    std::string out(int a, int b){
        //std::cout<<to_string(a)<<'\n';
        //std::cout<<to_string(a)+"->"+to_string(b)<<'\n';
        if(a>=b){
            return to_string(a);
        }
        /*if(b<a){
            return to_string(b)+"->"+to_string(a);
        }*/
        return to_string(a)+"->"+to_string(b);
    }
public:
    vector<string> summaryRanges(vector<int>& nums) {
        std::vector<std::string> result;
        if(nums.empty()){
            return result;
        }
        /*if(nums.size()==1){
            result.push_back(to_string(nums))
        }*/
        std::sort(nums.begin(),nums.end());//algorithm header file
        /*for(auto ob:nums){
            std::cout<<ob;
        }*/
        int last=nums[0];
        int buffer_front=0,buffer_back=0;
        int now_status=0;
        for(auto ob=nums.begin();ob!=nums.end();++ob){
            //std::cout<<"ob "<<*ob<<" //front "<<buffer_front<<" back "<<buffer_back<<'\n';
            //||buffer_front>=buffer_back
            if(now_status==0){
                buffer_front=*ob;
                buffer_back=*ob;
                now_status=1;
                continue;
            }else{
                if(buffer_back+1!=*ob){
                    result.push_back(out(buffer_front,buffer_back));
                    buffer_front=*ob;
                    buffer_back=*ob;
                    now_status=2;
                    if(ob==nums.end()-1){
                        //std::cout<<"facing last\n";
                        result.push_back(out(buffer_front,*ob));
                        now_status=2;
                    }
                }else{
                    if(ob==nums.end()-1){
                        //std::cout<<"facing last\n";
                        result.push_back(out(buffer_front,*ob));
                        now_status=2;
                    }else{
                        buffer_back=*ob;
                        now_status=1;
                    }
                }
            }
        }
        if(now_status==1){
            result.push_back(out(buffer_front,buffer_back));
        }
        
        return result;
    }
};