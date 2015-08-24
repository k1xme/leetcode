#include <vector>
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (postorder.size() == 0) return {};
        int in_pos = 0, post_pos = 0;
         
    }
    
    TreeNode* build(vector<int>& inorder, int in_begin, int in_end,
                    vector<int>& postorder) {
        
        if (in_begin==in_end) {
            postorder.pop_back();
            return new TreeNode(inorder[in_begin]);
        }
        
        TreeNode *root = new TreeNode(postorder.back());
        int root_index=-1;
        
        for (int i = in_begin; i <= in_end; ++i) {
            if (inorder[i] == root->val) {
                root_index = i;
                break;
            }
        }

        if (root_index == -1) return NULL;
        postorder.pop_back();
        root->right = build(inorder, root_index+1, in_end, postorder);

        root->left = build(inorder, in_begin, root_index-1, postorder);
        
        return root;
    }
};

int main(int argc, char const *argv[])
{
    vector<int> in, post;
    in.push_back(1);
    in.push_back(2);
    in.push_back(3);
    in.push_back(4);
    post.push_back(2);
    post.push_back(1);
    post.push_back(4);
    post.push_back(3);
    Solution sol;
    TreeNode *r = sol.buildTree(in, post);
    return 0;
}