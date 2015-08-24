#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() < 3) return nums.size();
        int i = 2;

        for (auto n: nums)
        {
            if (n > nums[i-2])
            {
                nums[i++] = n;
            }
        }
        return i;
    }
};
int main()
{ 	
	// string s = "0000";
	Solution sol;
	// int result = sol.restoreIpAddresses(s);
    // cout << result << endl;
    vector<int> dd;
    dd.push_back(1);
    dd.push_back(1);
    dd.push_back(1);
    dd.push_back(2);
    dd.push_back(2);
    // dd.push_back(2);
    dd.push_back(3);
    int length = sol.removeDuplicates(dd);
    
    for (auto i=0; i < length; i++){
        cout << dd[i] <<endl;
    }
	return 0;
}