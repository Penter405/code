#include <bits/stdc++.h>
int main(){
    std::vector<int> v={1,2,3};
    std::map<std::vector<int>, std::string> hash;
    std::map<std::string, std::string> hash2;
    hash[v]="im penter";
    hash2["whats_up"]="im penter";
    std::cout<<hash[v]<<std::endl;
    std::cout<<hash2["whats_up"]<<std::endl;
}