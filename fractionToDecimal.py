"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)". 
"""

"""
Idea: If the numerator is greater than the denominator, use numerator/denominator
as the integral part of the final result, else set the integral part to 0 and times with 10
and repeat this step until numerator is greater. Then get the remainer of 
numerator/denominator, if it's 0 we're done, else times it with 10 and repeat
the above steps until we find a repeating pattern or the remainer is 0.
"""

"""
Pitfalls:
1. Will the denominator be 0? Is the input always valid?
2. Will the result be a non-repeating non-terminal fraction?
3. If so, what is the expecting behavior of this program?
4. How to deal with negative number?
"""

class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        elif numerator == denominator:
            return "1"

        # All the remainers and the coresponding index in result seen so far.
        seen_remainers = {}

        # Insert the integeral part.
        sign = "-" if numerator / denominator < 0 else ""

        numerator = abs(numerator)
        denominator = abs(denominator)
        result = sign + str(numerator/denominator)
        remainer = numerator % denominator

        if remainer != 0:
            result += "."
        else:
            return result

        # Record the remainer and its index in result.
        seen_remainers[remainer] = len(result)

        while remainer != 0:
            result += str(remainer*10 / denominator)
            remainer = remainer*10 % denominator

            # If the reaminer has shown up before, then we find a pattern.
            if remainer in seen_remainers:
                index = seen_remainers[remainer]
                result = result[:index] + "(" + result[index:] + ")"
                break

            # Else we just record the new remainer's index and keep going.
            seen_remainers[remainer] = len(result)

        return result

s = Solution()

assert s.fractionToDecimal(2, 3) == "0.(6)"
assert s.fractionToDecimal(1, 3) == "0.(3)"
assert s.fractionToDecimal(1, 30) == "0.0(3)"
assert s.fractionToDecimal(500, 10) == "50"
assert s.fractionToDecimal(-50, 8) == "-6.25"






