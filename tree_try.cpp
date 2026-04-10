#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
struct tree{
	int value;
	*tree left=nullptr;
	*tree right=nullptr;
};


int main(int argc, char** argv) {
	std::cout<<"hello world\n";
	int x=5;
	std::cin>>x;
	std::cout<<x;
	tree x;
	x.value=5;
	std::cout<<x.value<<'\n'<<&x<<'\n';
	return 0;
}
