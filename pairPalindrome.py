def isPalindrome(s):
	left,right = 0, len(s)-1

	while left <= right:
		if s[left]!= s[right]:
			return False
		left += 1
		right -= 1

	return True

def pairPalindromes(words):
	pairs = [(words[i], words[j]) for i in range(len(words)) for j in range(i+1, len(words))]

	for pair in pairs:
		if isPalindrome(pair[0]+pair[1]) or isPalindrome(pair[1]+pair[0]):
			print pair


pairPalindromes(['cigar', 'tragic', 'xenon', 'none','aabbaabb', 'bbaabbaa', 'a', 'bba'])