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
//inorder searching can make the left<root<right struct very likely sorted
private:
    //int range is nagative 2B to 2Billion
    std::vector<int> range;
    int recursion(TreeNode* root){
            if((*root).left!=nullptr){
                recursion((*root).left);
            }
            range.push_back((*root).val);
            if((*root).right!=nullptr){
                recursion((*root).right);
            }
            return 0;
        }

public:
    int getMinimumDifference(TreeNode* root) {
        recursion(root);
        int result=-1;
        std::sort(range.begin(),range.end());//header file:algorithm
        /*for(auto it:range){
            std::cout<<it<<' ';
        }*/
        for(int i=0;i+1<range.size();++i){
            if(result==-1 || range[i+1]-range[i]<result){
                result=range[i+1]-range[i];
            }
        }
        return result;
    }
};