def isPalindrome(s):
	i, j = 0, len(s)-1

	while i <= j:
		if s[i] != s[j]: return False
		i += 1
		j -= 1

	return True

def allPalindrome(s):
	if not s: return s

	n = len(s)
	count = 0
	
	# O(n^3)
	for i in range(n):
		# find odd-length palindromes.
		span = 0

		while i - span >= 0 and i + span < n and isPalindrome(s[i-span:i+span+1]):
			count += 1
			span += 1
		span = 0
		while i - span -1 >= 0 and i + span < n and isPalindrome(s[i-span-1:i+span+1]):
			count += 1
			span += 1

	return count

print allPalindrome('aba')
print allPalindrome('abba')