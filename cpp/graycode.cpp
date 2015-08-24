#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> grayCode(int n) {
      vector<int> result;
      if (n==0) {
        result.push_back(0);
        return result;
      }

      result.push_back(0);
      result.push_back(1);
      int flip = 0;

      for (int i = 1; i < n; ++i)
       {  
        vector<int> temp;
        for (vector<int>::iterator i = result.begin(); i < result.end(); ++i)
          {
            if (flip==0) {
              temp.push_back(*i<<1);
              temp.push_back((*i<<1)+1);
            }
            else {
              temp.push_back((*i<<1)+1);
              temp.push_back(*i<<1);
            }
            flip = flip ^ 1;
          }
        result = temp;
       }
      return result;
    }
};

int main()
{
  sd
  Solution sol;
  vector<int> v = sol.grayCode(0);
  for (vector<int>::iterator i = v.begin(); i != v.end(); ++i)
  {
    cout << *i << endl;
  }
  return 0;
}