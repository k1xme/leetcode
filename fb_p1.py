#Problem 1
'''
**1** You're given a dictionary of strings, and a key. Check if the key is composed of an arbitrary number of concatenations of strings from the dictionary.
For example:
dictionary: "world", "hello", "super", "hell" key: "helloworld" --> return true key: "superman" --> return false key: "hellohello" --> return true
'''

# Solution 1, basic DP with complexity of O(n^2).


def is_concantention(words, key):
	if not key: return False
	stack = []
	wordbag = set()
	
	for word in words: wordbag.add(word)

	word_start = 0
	i = 1
	while i <= len(key):
		if key[word_start:i] in wordbag:
			if i == len(key): return True
			stack.append((word_start, i))
			word_start = i
		elif i == len(key):
			if not stack: break
			word_start, i = stack.pop()
		i += 1

	return False

	
print is_concantention(["hello", "world"], "worldhello")
print is_concantention(["ice", "icecream"], "icecreamicei")
print is_concantention(["leet", "code"], "leetcode")



