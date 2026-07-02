class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            node = node.children[ch]

        node.is_end = True

        
    def search(self, word: str) -> bool:
        node = self
        for i, ch in enumerate(word):
            if ch == '.':
                for child in node.children.values():
                    if child.search(word[i+1:]):
                        return True
                    
                return False

            elif ch not in node.children:
                return False
            node = node.children[ch]
        
        # if node.is_end == True:
        #     return True
        
        return node.is_end
        
        
