class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrs = {}
        self.dictionary = dictionary
        for word in dictionary:
            abbr = self.getAbbr(word)
            if abbr not in self.abbrs:
                self.abbrs[abbr] = 1
            else:
                self.abbrs[abbr] += 1
        

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return True
        abbr = self.getAbbr(word)
        if word in self.dictionary:

            return self.abbrs[abbr] < 2

        return abbr not in self.abbrs
        
    def getAbbr(self, word):
        if len(word) < 3:
            return word
        return word[0] + str(len(word)-2) + word[-1]
        

# Your ValidWordAbbr object will be instantiated and called as such:
vwa = ValidWordAbbr(['hello'])
print vwa.isUnique("hello")
# vwa.isUnique("anotherWord")