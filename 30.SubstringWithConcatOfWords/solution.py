# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def checkSubstring(string: str, words: List[str]) -> bool:
            length = len(words[0])
            l = len(string)
            tokens = []
            for i in range(0, l, length): # Tokenize the string into words
                tokens.append(string[i: i + length])
            for word in tokens:
                if word in words:
                    words.remove(word)
                else:
                    return False
            if len(words) == 0:
                return True
            return False

        indices = []
        l = len(s)
        substr_len = len(words) * len(words[0])
        for i in range(l):
            string = s[i:i+substr_len]
            if checkSubstring(string, words.copy()):
                indices.append(i)
            

        return indices