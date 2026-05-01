#include <bits/stdc++.h>
void initialize(std::unordered_map<int,int>& to_do){
    for(int i=0;i<10;++i){
        to_do[i]=i*10;
        std::cout<<"doing "<<i<<'\n';
    }

}
int main(){
    std::unordered_map<int,int> to_do;
    initialize(to_do);
    int i=0;
    for(auto& it:to_do){
        if(i==0){
            to_do.erase(5);
        }
        std::cout<<(it).first<<'\n';
    }
    return 0;
}