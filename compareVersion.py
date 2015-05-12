class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        version1_splitted = map(float, version1.split('.'))
        version2_splitted = map(float, version2.split('.'))
        
        version1_len = len(version1_splitted)
        version2_len = len(version2_splitted)
        
        for v1, v2 in zip(version1_splitted, version2_splitted):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        # The prefixes of these two versions are equal.
        # So the longer one is the higher version.
        if version1_len > version2_len:
            for i in range(version2_len, version1_len):
                if version1_splitted[i] > 0:
                    return 1
            return 0
        elif version1_len < version2_len:
            for i in range(version1_len, version2_len):
                if version2_splitted[i] > 0:
                    return 1
            return 0            
s = Solution()          
print s.compareVersion('1', '1.1')