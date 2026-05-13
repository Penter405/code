/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/


//same solution as 116. my solution work on both question.
class Solution {
private:
    std::vector<Node*> node_order;
    int size=-1;
    int recursion(Node* root, int level){
        if(root==nullptr){
            return 0;
        }
        //std::cout<<"im node"<<(*root).val<<".  ";
        if(size<level){
            node_order.push_back(root);
            ++size;
        }else{
            (*root).next=node_order[level];
            node_order[level]=root;
            //std::cout<<"my next is"<<(*(*root).next).val<<"\n";
        }
        recursion((*root).right, level+1);
        recursion((*root).left, level+1);
        return 0;
    }
public:
    Node* connect(Node* root) {
        recursion(root,0);
        return root;
    }
};