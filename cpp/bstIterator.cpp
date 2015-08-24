#include <vector>
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };
 
class BSTIterator {
private:
    vector<TreeNode*> stack;
    
public:
    BSTIterator(TreeNode *root) {
        appendLeftChildren(root);
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !stack.empty();
    }

    /** @return the next smallest number */
    int next() {
        TreeNode *v = stack.back();
        stack.pop_back();
        appendLeftChildren(v->right);
        return v->val;
        
    }
    
    void appendLeftChildren(TreeNode *root) {
        if (root == NULL) return;
        stack.push_back(root);
        appendLeftChildren(root->left);
    }
};

int main(int argc, char const *argv[])
{
    TreeNode root = (5), left = (4), right = (6);
    root.left  = &left;
    root.right = &right;
    BSTIterator iter(&root);
    cout << iter.next() << endl;
    cout << iter.next() << endl;
    cout << iter.next() << endl;
    return 0;
}