class Trie:
    class Node:
        def __init__(self):
            self.is_end = False
            self.next = [None] * 26

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not cur.next[i]:
                cur.next[i] = self.Node()
            cur = cur.next[i]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.next[i]:
                cur = cur.next[i]
            else:
                return False
        return cur.is_end
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if cur.next[i]:
                cur = cur.next[i]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
