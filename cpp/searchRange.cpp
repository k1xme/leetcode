//
//  searchRange.cpp
//  
//
//  Created by Kexi on 7/30/15.
//
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        return search(nums, target, 0, nums.size());
    }

    vector<int> search(vector<int>& nums, int target, int left, int right) {
        vector<int> v(2);
        v[0] = -1;
        v[1] = -1;
        
        if (left > right || (left == right && nums[left] != target)) return v;

        int mid = (right-left)/2 + left;
        
        if (nums[mid] == target) {
            v[0] = mid;
            v[1] = mid;
            vector<int> lr = search(nums, target, left, mid-1);
            vector<int> rr = search(nums, target, mid+1, right);
            if (lr[0] != -1) v[0] = lr[0];
            if (rr[1] != -1) v[1] = rr[1];
            return v;
        }
        
        if (nums[mid] < target) return search(nums, target, mid+1, right);

        return search(nums, target, left, mid-1);
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> v, r;
    v.push_back(1);
    v.push_back(1);
    v.push_back(1);
    v.push_back(1);
    v.push_back(1);
    v.push_back(1);
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    int target = 1;
    r = s.searchRange(v, target);
    cout << "result: ["<< r[0] << ", " << r[1] << "]" << endl;

    return 0;
}