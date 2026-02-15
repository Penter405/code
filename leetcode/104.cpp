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
public:
    int maxDepth(TreeNode* root) {
        if(!(root)){
            //if self is nullptr, which is not node, but is endding sign
            return 0;
        }
        //make sure ererything you need can be control in this block
        int l_node=1+maxDepth((*root).left);//1 is self depth, maxDepth is child length
        int r_node=1+maxDepth((*root).right);

        return std::max(l_node,r_node);//max function is belong to Algorithm header file
    }
};