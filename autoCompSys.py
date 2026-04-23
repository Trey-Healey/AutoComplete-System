class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        current.is_end_of_word = True

    def search_prefix(self, prefix):
        current = self.root

        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]

        return current

    def collect_words(self, node, current_word, results):
        if node.is_end_of_word:
            results.append(current_word)

        for char, child in node.children.items():
            self.collect_words(child, current_word + char, results)


class AutocompleteSystem:
    def __init__(self):
        self.trie = Trie()

    def load_dictionary(self, filename):
        with open(filename, "r") as file:
            for line in file:
                word = line.strip()
                self.trie.insert(word)

    def get_suggestions(self, prefix):
        node = self.trie.search_prefix(prefix)

        if node is None:
            return []

        results = []
        self.trie.collect_words(node, prefix, results)
        return results


# -------- MAIN --------
def main():
    system = AutocompleteSystem()
    system.load_dictionary("dictionary.txt")

    while True:
        prefix = input("Enter a prefix (or 'exit'): ")

        if prefix.lower() == "exit":
            break

        suggestions = system.get_suggestions(prefix)

        if not suggestions:
            print("No suggestions found")
        else:
            for word in suggestions:
                print(word)


if __name__ == "__main__":
    main()
