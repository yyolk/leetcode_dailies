# https://leetcode.com/problems/replace-words/


class TrieNode:
    def __init__(self):
        # Initialize each node with a dictionary for children and a boolean to mark the end of a word
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        # Initialize the root of the trie
        self.root = TrieNode()

    def insert(self, word):
        # Insert a word into the trie
        node = self.root
        for char in word:
            # Traverse the trie, creating nodes as necessary
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # Mark the end of a word
        node.is_end = True

    def search_shortest_prefix(self, word):
        # Search for the shortest prefix of a word in the trie
        node = self.root
        prefix = []
        for char in word:
            # If the character is not in the children, return the original word
            if char not in node.children:
                return word
            node = node.children[char]
            prefix.append(char)
            # If we reach the end of a word in the trie, return the prefix
            if node.is_end:
                return "".join(prefix)
        # If no prefix is found, return the original word
        return word


class Solution:
    """648. Replace Words

    In English, we have a concept called **root**, which can be followed by some other
    word to form another longer word - let's call this word **derivative**. For example,
    when the **root** `"help"` is followed by the word `"ful"`, we can form a derivative
    `"helpful"`.

    Given a `dictionary` consisting of many **roots** and a `sentence` consisting of
    words separated by spaces, replace all the derivatives in the sentence with the
    **root** forming it. If a derivative can be replaced by more than one **root**,
    replace it with the **root** that has **the shortest length**.

    Return *the `sentence`* after the replacement.

    """

    def replace_words(self, dictionary: list[str], sentence: str) -> str:
        # Create a trie and insert all the roots from the dictionary
        trie = Trie()
        for root in dictionary:
            trie.insert(root)

        # Split the sentence into words
        words = sentence.split()
        # Replace each word with its shortest root prefix if available
        for i in range(len(words)):
            words[i] = trie.search_shortest_prefix(words[i])

        # Join the words back into a sentence
        return " ".join(words)

    replaceWords = replace_words
