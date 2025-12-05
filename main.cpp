#include <iostream>
using namespace std;
class human{
    public:
    int hight,kg;
    char name[11];
    void output_name(){
       cout<<name<<"\n";
    }
};

int math(){
    human pencel;
    pencel.kg=99;
    cout<<pencel.kg<<"\n";
    cout<<"enter your name(under 11 character):";cin>>pencel.name;
    pencel.output_name();
    return 0;
}

int first_try(){
    int x;
    cout<<"enter a integer:";cin>>x;
    cout<<"your integer is :"<<x<<"\n";
    cout<<"done\n";
    return 0;
}

int main(){
    first_try();
    math();
    return 0;
}
