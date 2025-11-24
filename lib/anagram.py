# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, word_list):
        if not isinstance(word_list, list):
            raise ValueError("Input must be a list of strings")
        return [word for word in word_list if self.is_anagram(word)]

    def is_anagram(self, other_word):
        if not isinstance(other_word, str):
            raise ValueError("Input must be a string")
        return sorted(self.word) == sorted(other_word.lower())

    def __str__(self):
        return f"Anagram of: {self.word}"   
    pass