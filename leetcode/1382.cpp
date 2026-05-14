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
/*
class Solution {
public:
    TreeNode* balanceBST(TreeNode* root) {
        
    }
};
*/
class Solution {
private:
    int find_index(int parent_A, int parent_B) {
        if (parent_A + 1 == parent_B) {
            return -1; // no node in mid, return indicator
        }
        int bot = parent_A + parent_B;
        if (bot % 2 != 0) {
            return bot / 2 + 1;
        }
        return bot / 2;
    }

    std::vector<int> bst_order;

    int inorder_search(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        inorder_search((*root).left);
        bst_order.push_back((*root).val);
        inorder_search((*root).right);
        return 0;
    }

    TreeNode* recursion(int p_A, int p_B) {
        int bot = find_index(p_A, p_B);
        if (bot == -1) {
            return nullptr;
        }

        TreeNode* me = new TreeNode(bst_order[bot]);
        (*me).left = recursion(p_A, bot);
        (*me).right = recursion(bot, p_B);
        return me;
    }

public:
    TreeNode* balanceBST(TreeNode* root) {
        inorder_search(root);
        return recursion(-1, bst_order.size());
    }
};