class GrammarStats:
    def __init__(self):
        self.correct = 0
        self.incorrect = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if text == "":
            raise Exception("No text!")
        else:
            if text[-1] in '!?.' and text[0].isupper():
                self.correct += 1
                return True
            else:
                self.incorrect += 1
                return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.correct == 0 and self.incorrect == 0:
            raise Exception("No texts given!")
        else:
            return 100 * (self.correct / (self.correct + self.incorrect))