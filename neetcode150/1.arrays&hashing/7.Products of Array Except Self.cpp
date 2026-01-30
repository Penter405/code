#include <iostream>
#include <vector>


class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int size=nums.size();
        //prefix ,postfix. and result[i] = prefix[i]*postfix[i]
        //remember from 0, to first element you see , and the second last element you see.
        //we need create two iterator, prefix is normal, postfix is reverse.
        std::vector<int> prefix,postfix,result;
        prefix.push_back(1);
        postfix.push_back(1);
        for(auto it=nums.begin()-1;;){
            if(++it==nums.end()-1){
                break;
            }
            //std::cout<<*(prefix.end()-1)<<" times "<<*it<<'\n';
            prefix.push_back((*(prefix.end()-1))*(*it));
        }
        //std::cout<<"next\n";
        for(auto it=nums.rbegin()-1;;){
            if(++it==nums.rend()-1){
                break;
            }
            //std::cout<<*(postfix.end()-1)<<" times "<<*it<<'\n';
            postfix.push_back(*(postfix.end()-1)*(*it));
        }
        auto pre_cheak= prefix.begin();
        auto post_cheak= postfix.rbegin();
        for(int i=0;i<size;++i){
            result.push_back((*pre_cheak)*(*post_cheak));

            ++pre_cheak;
            ++post_cheak;
        }
        return result;
    }
    
};
//follow up: make prefix work into for loop of pushing back result 
//not finishing solution two below
//i think linked_list not allow method "push_back" and some same name from vector. we need to go cppreference.com
//now we see postfix from back to front. but add result from begin to end. this make problem because we change value of will be using element, which is iterator of postfix will use.
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int size=nums.size();
        std::linked_list<int> postfix;
        postfix.push_back(1);
        for(auto it=nums.rbegin()-1;;){
            if(++it==nums.rend()-1){
                break;
            }
            std::cout<<*(postfix.end()-1)<<" times "<<*it<<'\n';
            postfix.push_back(*(postfix.end()-1)*(*it));
        }
        //uto pre_cheak= prefix.begin();
        int pre_cheak=1;
        auto see=nums.begin();
        auto post_cheak= postfix.rbegin();
        for(int i=0;i<size;++i){
            std::cout<<"pre times post: "<<pre_cheak<<" * "<<*post_cheak<<'\n';
            postfix[i]=pre_cheak*(*post_cheak);
            pre_cheak*=*see;
            ++see;
            //++pre_cheak;
            ++post_cheak;
        }
        return postfix;
    }
    
};
//follow up: make prefix work into for loop of pushing back result 
