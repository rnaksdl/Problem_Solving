'''
151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
'''

class Solution1:
    def reverseWords(self, s: str) -> str:
        
        # init word and words
        word = ""
        words = []

        # iter s
        for c in s:

            # if sees empty char
            if c == " ":
                # if we have added anything to word
                if word != "":
                    # append word to words
                    words.append(word)
                    # and reset word
                    word = ""
                continue
            else:
                # char not empty, add to word
                word += c
        
        # after iteration, if word isn't empty append to words and reset word
        if word != "":
            words.append(word)
            word = ""

        # init result
        result = ""
        # iter words backwords
        for i in range(len(words) - 1, -1, -1):
            # add word to result
            result += words[i]
            # add spaces in between words except for the last word (first, sice it's reversed)
            if i != 0:
                result += " "

        return result

'''
first attempt!
very slow tho..
'''

