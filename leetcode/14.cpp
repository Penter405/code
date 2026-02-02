class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        //remenber all from first element
        std::string result="";
        //char seeing;
        auto iter=strs.begin();
        int size=-1;
        
        for(auto iter=strs[0].begin();iter<strs[0].end();++iter){
            //seeing=*iter;
            ++size;
            for(auto element=strs.begin()+1;element<strs.end();++element){
                if((*element)[size]!=*iter){
                    return result;
                }
            }
            result+=*iter;
        }
        
        return result;
    }
};