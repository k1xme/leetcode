#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: The maximum number inside the window at each moving.
     */
    vector<int> maxSlidingWindow(vector<int> &nums, int k) {
        vector<int> result;
        if(nums.empty() || k > nums.size()) return result;

        int maxInWin = nums[0];
        for (int i = 0; i < k; ++i) maxInWin = max(nums[i], maxInWin);
        result.push_back(maxInWin);

        for (int i = k; i < nums.size(); ++i)
        {
            if (nums[i-k] != maxInWin) {
                maxInWin = max(maxInWin, nums[i]);
                result.push_back(maxInWin);
                continue;
            }
            // cout << nums[i] << " " << maxInWin << endl;
            if (nums[i] < maxInWin) {
                maxInWin = nums[i-k+1];
                for (int j=i-k+1; j <= i; ++j) maxInWin = max(maxInWin, nums[j]);
            }
            else maxInWin = nums[i];
            result.push_back(maxInWin);
        }

        return result;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(7);
    v.push_back(7);
    v.push_back(2);
    v = sol.maxSlidingWindow(v, 3);

    for (vector<int>::iterator i = v.begin(); i != v.end(); ++i)
    {
        cout << *i << " ";   
    }
    return 0;
}
