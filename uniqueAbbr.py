class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrs = set()
        for word in dictionary:
            self.abbrs.add(self.getAbbr(word))
        

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            print "here"
            return True
        return word not in self.abbrs
    def getAbbr(self, word):
        if len(word) < 3:
            return word
        return word[0] + str(len(word)-2) + word[-1]

v = ValidWordAbbr(['dig'])
print v.getAbbr('dog')
print v.isUnique('dog')
