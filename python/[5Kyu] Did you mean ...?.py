"""
I'm sure, you know Google's "Did you mean ...?", when you entered a search term and mistyped a word. In this kata we want to implement something similar.
You'll get an entered term (lowercase string) and an array of known words (also lowercase strings). Your task is to find out, which word from the dictionary is most similar to the entered one. The similarity is described by the minimum number of letters you have to add, remove or replace in order to get from the entered word to one of the dictionary. The lower the number of required changes, the higher the similarity between each two words.
Same words are obviously the most similar ones. A word that needs one letter to be changed is more similar to another word that needs 2 (or more) letters to be changed. E.g. the mistyped term berr is more similar to beer (1 letter to be replaced) than to barrel (3 letters to be changed in total).
Extend the dictionary in a way, that it is able to return you the most similar word from the list of known words.

Code Examples:

fruits = Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry'])
fruits.find_most_similar('strawbery') # must return "strawberry"
fruits.find_most_similar('berry') # must return "cherry"

things = Dictionary(['stars', 'mars', 'wars', 'codec', 'codewars'])
things.find_most_similar('coddwars') # must return "codewars"

languages = Dictionary(['javascript', 'java', 'ruby', 'php', 'python', 'coffeescript'])
languages.find_most_similar('heaven') # must return "java"
languages.find_most_similar('javascript') # must return "javascript" (identical words are obviously the most similar)
I know, many of you would disagree that java is more similar to heaven than all the other ones, but in this kata it is ;)
"""

class Dictionary:
    def __init__(self, words):
        self.words = words

    def _levenshtein_distance(self, s1, s2):
        if len(s1) < len(s2):
            return self._levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)

        for i, char1 in enumerate(s1):
            current_row = [i + 1]

            for j, char2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[-1] + 1
                substitutions = previous_row[j] + (char1 != char2)
                current_row.append(min(insertions, deletions, substitutions))

            previous_row = current_row

        return previous_row[-1]

    def find_most_similar(self, term):
        min_distance = float('inf')
        most_similar_word = ""

        for word in self.words:
            distance = self._levenshtein_distance(term, word)

            if distance < min_distance:
                min_distance = distance
                most_similar_word = word

        return most_similar_word
