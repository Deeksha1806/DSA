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
    int diameter=0;
public:
  int dfs(TreeNode*node,int &diameter)
  {
   if(!node)
   return 0;
   int left=dfs(node->left,diameter);
   int right=dfs(node->right,diameter);
diameter=max(diameter,left+right);
return 1+max(left,right);

  }
    int diameterOfBinaryTree(TreeNode* root) {
        diameter=0;
        dfs(root,diameter);
        return diameter;
        
    }
};