/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    vector<string> result;
    int recursion(TreeNode* root, std::string my_dad){
        if(root==nullptr){
            return 0;
        }
        //std::cout<<"node value is "<<(*root).val<<'\n';
        std::string me;
        if(my_dad.empty()){
            me=to_string((*root).val);
        }else{
            me=my_dad+"->"+to_string((*root).val);
        }
        /*for(auto it:me){
            std::cout<<it;
        }
        */
        //std::cout<<'\n';
        if((*root).left==nullptr && (*root).right==nullptr){
            result.push_back(me);
        }else{
            recursion((*root).left,me);
            recursion((*root).right,me);
        }
        return 0;
    }
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        recursion(root, "");
        return result;
    }
};