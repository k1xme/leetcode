#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::vector<int> appearances;
        appearances.resize(256, -1);
        int left = 0, right = 0, max_len = 0;
        
        while (right < s.length()) {
            cout << appearances[0]<<endl;
            if (appearances[s[right]] >= left) {
                cout << appearances[s[right]]<<endl;
                left = appearances[s[right]] + 1;
            }
            
            appearances[s[right]] = right;
            max_len = max(max_len, right-left+1);
            right ++;
        }
        
        return max_len;
    }
};

int main(int argc, char **argv)
{
  map<char, int> appearances;
  string s = "c";
  Solution sol;
  cout << sol.lengthOfLongestSubstring(s) << endl;
  return 0;
}