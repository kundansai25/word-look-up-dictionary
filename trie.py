class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word.lower():
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word):
        curr = self.root
        for char in word.lower():
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def suggest(self, prefix):
        def dfs(node, path, suggestions):
            if node.is_end_of_word:
                suggestions.append(''.join(path))
            for char, child in node.children.items():
                dfs(child, path + [char], suggestions)

        curr = self.root
        for char in prefix.lower():
            if char not in curr.children:
                return []
            curr = curr.children[char]

        suggestions = []
        dfs(curr, list(prefix), suggestions)
        return suggestions