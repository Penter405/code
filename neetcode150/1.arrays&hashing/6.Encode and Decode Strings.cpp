#include <string>
#include <vector>
#include <iostream>

class Solution {
public:
    std::string encode(std::vector<std::string>& strs) {
        std::string result;
        const unsigned char key= 255,no_element=254,space_element=253;
        if(strs.empty()){
            result+=no_element;
            return result;
        }
        if(strs.size()==1&&strs[0]==""){
            result+=space_element;
            return result;
        }
        
        for(auto it =strs.begin();it!=strs.end();){
            //result+it;
            //std::cout<<*it<<",";
            result+=*it;
            if(++it!=strs.end()){
                result+=key;
            }
        }
        //std::cout<<"\n";
        return result;
    }

    std::vector<std::string> decode(std::string s) {
        //std::cout<<s;
        std::vector<std::string> result;
        const unsigned char key= 255,no_element=254,space_element=253;
        if(static_cast<unsigned char>(s[0])==no_element){
            return result;
        }

        if(static_cast<unsigned char>(s[0])==space_element){
            result.push_back("");
            return result;
        }
        
        //if(s.size()==0){
            //std::cout<<"size 0";
            //return result;
        //}
        result.push_back("");
        int time=0;
        for(auto it=s.begin();it!=s.end();++it){
            //std::cout<<"time:"<<time<<"guy"<<*it<<"\n";
            //std::cout<<it<<"\n";
            
            if(static_cast<unsigned char>(*it)==key){
                //std::cout<<"got";
                ++time;
                result.push_back("");
            }else{
                result[time]+=*it;
            }
        }
        //result.push_back(s);
        return result;
    }
};
//maybe i can learn that make vector point to a range of string.
//and question says string only include legal charater. we can use sign like "!".
//but, in this question , i learned about how change data type , maybe that dont change , but its a good why to know wheather ram binary value are same.