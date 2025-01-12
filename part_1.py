from pytrie import StringTrie


class Homework:
    def __init__(self):
        self.trie = StringTrie()

    def put(self, word, value=None):
        self.trie[word] = value

    def count_words_with_suffix(self, pattern: str) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string.")

        count = 0
        for key in self.trie.keys():
            if key.endswith(pattern):
                count += 1
        return count

    def has_prefix(self, prefix: str) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string.")

        return any(key.startswith(prefix) for key in self.trie.keys())


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

    print("All tests passed!")
