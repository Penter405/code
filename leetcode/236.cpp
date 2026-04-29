class Solution {
private:
    //std::unordered_map<int, int> dict; // the value of a tree node: the good the node has 1
    int lowest_legal_object_value;
    TreeNode* lowest_legal_object = nullptr;
    int p_value, q_value;

    void initialize(TreeNode* a, TreeNode* b) {
        p_value = (*a).val;
        q_value = (*b).val;
    }

    int recursion(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        int my_value = 0;
        int child_left = recursion(root->left);
        int child_right = recursion(root->right);

        if (root->val == p_value || root->val == q_value) {
            my_value = 1;
        }

        my_value += child_left + child_right;

        if (my_value >= 2) {
            if (lowest_legal_object == nullptr) {
                lowest_legal_object = root;
                lowest_legal_object_value = root->val;
            }/* else {
                if (root->val < lowest_legal_object_value) {
                    lowest_legal_object = root;
                    lowest_legal_object_value = root->val;
                }
            }*/
        }

        return my_value;
    }

public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        initialize(p, q);
        recursion(root);
        return lowest_legal_object;
    }
};