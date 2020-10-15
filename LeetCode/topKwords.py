# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        vals = {}
        for i in words:
            if i in vals.keys():
                vals[i] = vals[i]+1
            else:
                vals[i] = 0
        wordPairs = []
        for i in vals.keys():
            wordPairs.append((i, vals[i]))
        wordPairs.sort( key = lambda x: (-x[1], x[0]))
        vals = []
        for i in range(k):
            vals.append(wordPairs[i][0])
        return vals