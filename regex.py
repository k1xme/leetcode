def isMatch(s, p):
	# print s,p
	if not p: 
		return not s
	if not s:
		if p[-1] == '*': return isMatch(s, p[:-2])
		return False

	if p[-1] != '*':
		if p[-1] == s[-1] or p[-1] == '.':
			return isMatch(s[:-1], p[:-1])
		return False

	if p[-2] == s[-1] or p[-2] == '.':
		if isMatch(s, p[:-2]): return True

		for end in range(len(s)-1, -1, -1):
			if not (s[end] == p[-2] or p[-2] == '.'): break
			if isMatch(s[:end], p[:-2]): return True
		return False
	return isMatch(s, p[:-2])

# print isMatch('bba', 'a*')
# print isMatch("aab", "c*a*b")
# print isMatch("abasdasdasdsadasd", ".*")
# print isMatch("aaca", "ab*a*c*a")
# print isMatch("aaba" ,"ab*a*c*a")
print isMatch("bbab","b*a*")
# print isMatch("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s")
# print isMatch('aasdfasdfasdf', 'aasdf.*asdf.*asdf.*')
