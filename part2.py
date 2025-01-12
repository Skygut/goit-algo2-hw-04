from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(
            isinstance(s, str) for s in strings
        ):
            return ""  # Handle invalid input

        if not strings:
            return ""  # Handle empty list

        # Insert all words into the trie
        for word in strings:
            self.put(word)

        # Find the longest common prefix
        prefix = []
        current = self.root

        while current and len(current.children) == 1 and current.value is None:
            ((char, next_node),) = current.children.items()
            prefix.append(char)
            current = next_node

        return "".join(prefix)


if __name__ == "__main__":
    # Tests
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = ["one"]
    assert trie.find_longest_common_word(strings) == "one"

    print("All tests passed.")
