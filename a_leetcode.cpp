class Solution {
    private:
        unordered_map<char,char> hash;
            
            public:
                bool isPalindrome(string s) {
                        auto front=s.begin();
                                auto back=s.rbegin();
                                        for(;front!=s.end()&&back!=s.rend();){
                                                    std::cout<<*front<<"  "<<*back<<"\n";
                                                                while(*front==' '){
                                                                                if(++front==s.end()){
                                                                                                    return true;
                                                                                                                    }
                                                                                                                                }
                                                                                                                                            while(*back==' '){
                                                                                                                                                            if(++back==s.rend()){
                                                                                                                                                                                return true;
                                                                                                                                                                                                }
                                                                                                                                                                                                            }
                                                                                                                                                                                                                        if(*front!=*back){
                                                                                                                                                                                                                                        return false;
                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                ++front;
                                                                                                                                                                                                                                                                            ++back;
                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                            return true;
                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                                };
}