"""
Utility methods
"""


class Utils(object):
    """
    Utils
    """

    def __init__(self, wordlist):
        self.wordlist = wordlist

    def load_words(self):
        """

        :return:
        """
        with open(self.wordlist) as word_list:
            loaded_wordlist = set(word_list.read().split())

        return loaded_wordlist
