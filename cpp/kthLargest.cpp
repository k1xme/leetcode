#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return quickSelection(nums, 0, nums.size()-1, k-1);
    }
    
    int quickSelection(vector<int>& nums, int start, int end, int k) {
        if (start == end) return nums[start];
        int pivot = nums[end], storeIndex=start;
        
        for (int i=start; i < end; ++i) if (nums[i] > pivot) swap(nums, i, storeIndex++);
        swap(nums, end, storeIndex);
        
        if (storeIndex == k) {

            return nums[k];
        }
        if (storeIndex < k) return quickSelection(nums, storeIndex+1, end, k);
        return quickSelection(nums, start, storeIndex-1, k);
    }
    
    void swap(vector<int>& nums, int i, int storeIndex) {
        if (i==storeIndex) return;
        nums[i] ^= nums[storeIndex];
        nums[storeIndex] ^= nums[i];
        nums[i] ^= nums[storeIndex];
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    vector<int> v;
    v.push_back(2);
    v.push_back(1);
    cout << sol.findKthLargest(v, 1);
    return 0;
}