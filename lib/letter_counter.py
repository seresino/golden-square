# File: lib/letter_counter.py

class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 0
        for char in self.text:
            if not char.isalpha():
                continue
            if char.lower() in counter:
                counter[char.lower()] = counter.get(char.lower()) + 1
            else:
                counter[char.lower()] = 1
            if counter[char.lower()] > most_common_count:
                most_common = char.lower()
                most_common_count = counter[char.lower()]
        return [most_common_count, most_common]


counter = LetterCounter("Ruby Seresins")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]