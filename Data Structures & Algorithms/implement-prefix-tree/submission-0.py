class PrefixTree:

    def __init__(self):
        self.children = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        if word == "":
            self.isEnd = True
        elif word[0] in self.children:
            self.children[word[0]].insert(word[1:])
        else:
            temp = PrefixTree()
            self.children[word[0]] = temp
            temp.insert(word[1:])

    def search(self, word: str) -> bool:

        if word == "":
            return self.isEnd
        if word[0] in self.children:
            return self.children[word[0]].search(word[1:])
        return False

    def startsWith(self, prefix: str) -> bool:
        if prefix == "":
            return True
        if prefix[0] in self.children:
            return self.children[prefix[0]].startsWith(prefix[1:])
        return False
        
        