#include <bits/stdc++.h>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

//pre=[3,9,20,15,7]
// in=[9,3,15,20,7]
class Solution {
private:
    std::unordered_map<int,int> value_to_bst_index;
    std::unordered_map<int,int> bst_index_back_value;
    std::vector<int> bst_index_stack;//[val]
    std::unordered_map<int,TreeNode*> bst_to_object_pointer;//[val: object pointer]
    int initialize(std::vector<int>& inorder){
        int x=-1;
        for(auto it:inorder){
            ++x;
            value_to_bst_index[it]=x;
            bst_index_back_value[x]=it;
        }
        return 0;
    }
public:
    TreeNode* buildTree(std::vector<int>& preorder, std::vector<int>& inorder) {
        initialize(inorder);
        int index_stack;
        TreeNode* p;
        p=new TreeNode(preorder[0]);
        bst_index_stack.push_back(value_to_bst_index[preorder[0]]);
        index_stack=0;
        bst_to_object_pointer[value_to_bst_index[preorder[0]]]=(p);
        for(int i=1;i<preorder.size();++i){
            if(value_to_bst_index[preorder[i]]<bst_index_stack[index_stack]){
                //std::cout<<value_to_bst_index[preorder[i]]<<" < "<<bst_index_stack[index_stack]<<"\n";
                TreeNode* p_child;
                p_child=new TreeNode(preorder[i]);
                (*bst_to_object_pointer[bst_index_stack[index_stack]]).left=(p_child);
                //std::cout<<(*bst_to_object_pointer[bst_index_stack[index_stack]]).val<<" his left is "<<(*p_child).val<<"\n";
                bst_index_stack.push_back(value_to_bst_index[preorder[i]]);
                ++index_stack;
                bst_to_object_pointer[value_to_bst_index[preorder[i]]]=(p_child);
                
            }else{
                //now seeing must bigger than root, so we cheak which small
                //but not left could be someone's right
                //std::cout<<value_to_bst_index[preorder[i]]<<" > "<<bst_index_stack[index_stack]<<"\n";
                while(index_stack!=0 && value_to_bst_index[preorder[i]] >bst_index_stack[index_stack-1]){
                    //bst_index_stack smallest is 1, and 1-1=0, no address fetch wrong
                    //std::cout<<"we are seeing "<<value_to_bst_index[preorder[i]]<<" it more than "<<bst_index_stack[index_stack-1]<<"  so we should clear stack when it fetch to right?, if the node go to right, him self remove.\n";
                    bst_index_stack.pop_back();
                    --index_stack;
                }
                //add right to last element of bst_index_stack object
                TreeNode* p_child;
                p_child=new TreeNode(preorder[i]);
                (*bst_to_object_pointer[bst_index_stack[index_stack]]).right=(p_child);
                //std::cout<<(*bst_to_object_pointer[bst_index_stack[index_stack]]).val<<" his right is "<<(*p_child).val<<"\n";
                bst_index_stack[index_stack]=(value_to_bst_index[preorder[i]]);//origin is push back, but now we remove it self, because as one node's left and right has child, no more node can be his child again
                //++index_stack;
                //std::cout<<"hi";
                bst_to_object_pointer[value_to_bst_index[preorder[i]]]=(p_child);
            }
        }
        return p;
    }
};