#include <iostream>
#include <string>
#include <unordered_map>
class Solution {
public:
    int romanToInt(std::string s) {
        //if was last, map seocnde using
        int result=0;
        std::unordered_map<char,int> normal={
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D',500},
            {'M',1000}
        };
        std::unordered_map<std::string,int> special={
            {"IV",3},
            {"IX",8},
            {"XL",30},
            {"XC",80},
            {"CD",300},
            {"CM",800}
        };
        
        //int last_i=0,last_x=0,last_c=0;
        int last=0;
        for(auto it=s.begin();it<s.end();++it){
            if(last&&special.find(std::string(it-1, it+1))!=special.end()){
                //std::cout<<string(it-1, it+1)<<"  it is "<<special[string(it-1, it+1)]<<'n';
                result+=special[std::string(it-1, it+1)];
            }else{
                //std::cout<<*it<<"it is"<<normal[*it]<<'\n';
                result+=normal[*it];
            }
            if(*it=='I'||*it=='X'||*it=='C'){
                //std::cout<<"got you\n";
                last=1;
            }else{
                last=0;
            }
        }
        return result;
    }
};
//version two below
class Solution {
private:
    int cheak(int a,int b){
        int result=a-b;
        if(result<=0){
            return 0;
        }
        result%=10;
        result%=10;
        if(result<10){
            return 1;
        }
        return 0;
    }
public:
    int romanToInt(std::string s) {
        //if was last, map seocnde using
        int result=0;
        std::unordered_map<char,int> normal={
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D',500},
            {'M',1000}
        };
        /*std::unordered_map<std::string,int> special={
            {"IV",3},
            {"IX",8},
            {"XL",30},
            {"XC",80},
            {"CD",300},
            {"CM",800}
        };
        */
        //int last_i=0,last_x=0,last_c=0;
        int last=0;
        result+=normal[s[0]];
        last=result;
        for(auto it=s.begin()+1;it<s.end();++it){
            if(cheak(normal[*it],last)){
                //std::cout<<string(it-1, it+1)<<"  it is "<<cheak(normal[*it],last)<<'\n';
                //std::cout<<"reduce "<<last*2<<'\n';
                result-=last*2;
            }
            //std::cout<<*it<<"it is"<<normal[*it]<<'\n';
            last=normal[*it];
            result+=last;
            
            //std::cout<<last<<" last\n";
        }
        
        return result;
    }
};
//version three below
class Solution {
private:
    int cheak(int a,int b){
        //std::cout<<a<<"  "<<b;
        int result=a-b;
        if(result<=0){
            //std::cout<<"nagative";
            return 0;
        }
        if(b!=1&&b!=10&&b!=100){
            //std::cout<<b<<"not 1,10,100";
            return 0;
        }
        while(result/10>0){
            //std::cout<<result<<'\n';
            result/=10;
        }
        //std::cout<<result;
        if(result==4||result==9){
            return 1;
        }
        return 0;
    }
public:
    int romanToInt(std::string s) {
        //if was last, map seocnde using
        int result=0;
        std::unordered_map<char,int> normal={
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D',500},
            {'M',1000}
        };
        /*std::unordered_map<std::string,int> special={
            {"IV",3},
            {"IX",8},
            {"XL",30},
            {"XC",80},
            {"CD",300},
            {"CM",800}
        };
        */
        //int last_i=0,last_x=0,last_c=0;
        int last=0;
        result+=normal[*s.rbegin()];
        last=result;
        for(auto it=s.rbegin()+1;it<s.rend();++it){
            int now=normal[*it];
            //std::cout<<"<"<<now<<"  "<<last<<"  >"<<*it<<'\n';
            //cheak(now,last);
            if(cheak(last,now)){
                //std::cout<<string(it-1, it+1)<<"  it is "<<cheak(normal[*it],last)<<'\n';
                //std::cout<<"reduce "<<now<<'\n';
                result-=now;
            }else{
                
                result+=now;
            }
            last=now;
            //std::cout<<*it<<"it is"<<normal[*it]<<'\n';
            
            //std::cout<<last<<" last\n";
        }
        
        return result;
    }
};