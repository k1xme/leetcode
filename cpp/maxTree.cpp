
#include <vector>
#include <iostream>
using namespace std;

class TreeNode {
public:
    int val;
    TreeNode *left, *right;
    TreeNode(int val) {
        this->val = val;
        this->left = this->right = NULL;
    }
 };
 
class Solution {
public:
    /**
     * @param A: Given an integer array with no duplicates.
     * @return: The root of max tree.
     */
    TreeNode* maxTree(vector<int> A) {
        if (A.size() == 1) return new TreeNode(A[0]);
        return _maxTree(A, 0, A.size()-1);
        
    }
    TreeNode* _maxTree(vector<int> A, int start, int end) {
        if (start == end) return new TreeNode(A[start]);
        int root_index = start, max_n = A[start];
        
        for (int i=start; i <= end; ++i) {
            if (A[i] > max_n){
                max_n = A[i];
                root_index = i;
            }
        }
        
        TreeNode *root = new TreeNode(A[root_index]);
        if (start < root_index-1) root->left = _maxTree(A, start, root_index-1);
        if (root_index+1 < end) root->right = _maxTree(A, root_index+1, end);

        return root;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    vector<int> v;
    v.push_back(1);
    v.push_back(3);
    v.push_back(2);
    v.push_back(5);
    v.push_back(4);

    sol.maxTree(v);
    return 0;
}