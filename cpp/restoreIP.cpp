#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        if (s.length() == 0 || s.length() > 12) return {};
        vector<string> result;
        string addr;
        restore(s, 0, 0, addr, result);
        return result;
    }

    void restore(string s, int start, int parts, string tmp_addr, vector<string> &addrs) {
    	if (start == s.size() && parts == 4) {
    		addrs.push_back(tmp_addr);
    		return;
    	}
    	if(s.size()-start>(4-parts)*3) return;
        if(s.size()-start<(4-parts)) return;
    	
    	if (s[start] == '0') {
    		if (parts == 0) tmp_addr += s[start];
    		else tmp_addr = tmp_addr + "."+s[start];
    		restore(s, start+1, parts+1, tmp_addr, addrs);
    		return;
    	}

    	string part, new_addr;
    	for (int i = 1; i < 4; ++i)
    		{	
    			if (start+i > s.size()) break;
    			part = s.substr(start, i);
    			if (atoi(&part[0]) <= 255) {
    				if (parts == 0) new_addr = part;
    				else new_addr = tmp_addr+"."+part;
    				restore(s, start+i, parts+1, new_addr, addrs);
    			}
    		}

    	return;
    }
};

int main()
{ 	
	string s = "0000";
	Solution sol;
	vector<string> v = sol.restoreIpAddresses(s);
	for (int i = 0; i < v.size(); ++i)
	{
		cout << v[i] << endl;
	}
	
	return 0;
}