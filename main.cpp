#include <iostream>
class human{
    public:
    int hight,kg;
    char name[11];
    void output_name(){
       std::cout<<name<<"\n";
    }
};

int math(){
    human pencel;
    pencel.kg=99;
    std::cout<<pencel.kg<<"\n";
    std::cout<<"enter your name(under 11 character):";std::cin>>pencel.name;
    pencel.output_name();
    return 0;
}

int first_try(){
    int x;
    std::cout<<"enter a integer:";std::cin>>x;
    std::cout<<"your integer is :"<<x<<"\n";
    std::cout<<"done\n";
    return 0;
}

int main(){
    first_try();
    math();
    return 0;
}
