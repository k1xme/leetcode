# This question is related to FSM.
# And we can optimize and make the program
# clearer by setup more flags to indicate different states.

# state is one of:
# - 0, stands for the initial state that expects '.', '+', '-', number.
# - 1, stands for the state that expects number or '.'.
# - 2, stands for the state that expects only number.
# - 3, stands for the state that expects '.', 'e' or number.
# - 4, stands for the state that expects number or 'e'.
# - 5, stands for the state that expects number, '-' or '+'.
# - 6, stands for the state that expects number.
# - 7, stands for the state that expects number or 'e'.
# - 8, stands for the state that expects number.

# ALL VALID INPUTS
POINT = '.'
POSITIVE = '+'
NEG = '-'
E = 'e'

class Solution:
    # @param {string} s
    # @return {boolean}
    
    def isNumber(self, s):
        state = 0
        s = s.strip()

        for c in s:
            if state == 0:
                if c in [POSITIVE, NEG]:
                    state = 1
                elif c == POINT:
                    state = 2
                elif c >= '0' and c <= '9':
                    state = 3
                else:
                    return False

            elif state == 1:
                if c == POINT:
                    state = 2
                elif c >= '0' and c <= '9':
                    state = 3
                else:
                    return False

            elif state == 2:
                if c >= '0' and c <= '9':
                    state = 4
                else:
                    return False

            elif state == 3:
                if c == E:
                    state = 5
                elif c == POINT:
                    state = 7
                elif c >= '0' and c <= '9':
                    continue
                else:
                    return False

            elif state == 4:
                if c == E:
                    state = 5
                elif c >= '0' and c <= '9':
                    continue
                else:
                    return False

            elif state == 5:
                if c in [POSITIVE, NEG]:
                    state = 6
                elif c >= '0' and c <= '9':
                    state = 8
                else:
                    return False

            elif state == 6:
                if c >= '0' and c <= '9':
                    state = 8
                else:
                    return False

            elif state == 7:
                if c == E:
                    state = 5
                elif c >= '0' and c <= '9':
                    continue
                else:
                    return False
            elif state == 8:
                if c >= '0' and c <= '9':
                    continue
                else:
                    return False

        if state in [0, 2, 5, 6]:
            return False

        return True

s = Solution()
print s.isNumber('3.')