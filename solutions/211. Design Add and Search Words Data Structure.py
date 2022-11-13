class TrieNode:
    def __init__(self):
        self.end = False
        self.next = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.next:
                cur.next[c] = TrieNode()
            cur = cur.next[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def helper(i, cur):
            if i == len(word):
                return cur.end
            c = word[i]
            if c == '.':
                for node in cur.next.values():
                    if helper(i + 1, node):
                        return True
                return False
            if c not in cur.next:
                return False
            return helper(i + 1, cur.next[c])
        return helper(0, self.root)
