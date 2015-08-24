#include <iostream>
#include <string>
using namespace std;


class Solution {
public:
    string countAndSay(int n) {
     string num = "1", nextNum = "";
     char cur;
     int count = 1;
     
     for (int i = 1; i < n; ++i) {
        for (int j=0; j < num.length(); ++j) {
            if ( j+1 < num.length() && num[j] == num[j+1]) ++ count;
            else {
                nextNum += char(count + '0');
                nextNum += + num[j];
                count = 1;
            }
        }
        num = nextNum;
        nextNum = "";
     }
     
     return num;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    cout << sol.countAndSay(3) << endl;
    return 0;
}