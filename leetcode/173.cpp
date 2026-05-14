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
class BSTIterator {
private:
    std::vector<int> inorder_traval;
    int index=-1;
    int max_index;
    int recursion(TreeNode* root){
        if(root==nullptr){
            return 0;
        }
        recursion((*root).left);
        inorder_traval.push_back((*root).val);
        recursion((*root).right);
        return 0;
    }
public:
    BSTIterator(TreeNode* root) {
        //std::cout<<(*root).val;
        //std::cout<<(*(*root).left).val;
        //do inorder traval
        recursion(root);
        max_index=inorder_traval.size()-1;
    }
    
    int next() {
        return inorder_traval[++index];
    }
    
    bool hasNext() {
        return index<max_index;
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */