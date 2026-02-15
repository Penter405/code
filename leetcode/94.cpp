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
    std::vector<int> result;

    int inorder_searching(TreeNode* root){
        //std::cout<<"seeing element value:"<<(*root).val<<"\n";
        //if(!root){
            //return 
        //}
        //seeing must be a node;
        if((*root).left){
            int left_node=inorder_searching((*root).left);
            //result.push_back(left_node); facing double push_back when seeing not root of tree.
        }
        result.push_back((*root).val);
        if((*root).right){
            int right_node=inorder_searching((*root).right);
            //result.push_back(right_node);
        }
        return (*root).val;
    }
public:
    vector<int> inorderTraversal(TreeNode* root) {
        if(!root){
            return result;
        }
        inorder_searching(root);
        return result;
    }
};