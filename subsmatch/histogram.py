
from collections import Counter

import numpy as np


class Histogram:

    def __init__(self, sequence, w) -> None:
        """
        Input sequence is a list of strings.
        w defines the length of each pattern.
        """

        self.sequence = np.array(sequence)
        self.w = w
        self.N = len(sequence)

        # Compute histogram
        self.table = self._getFrequency()

    def distance(self, other):
        """
        Computes the distance between self and 
        another Histogram object.
        """

        half = self.table - other.table
        other_half = other.table - self.table
        absolute_difference = half + other_half

        return 1/2 * sum(absolute_difference.values())

    def _getFrequency(self):
        """
        Given a list of symbols, store the 
        frequency of each subsequence.
        """

        # Counter object
        freq = Counter()

        # Indexer matrix to extract all subsequences of
        # length n with a stride of 1
        window_indexer = np.array(
            np.expand_dims(np.arange(self.w), 0) +
            np.expand_dims(np.arange(self.N - self.w + 1), 0).T
        )
        print('self.sequence =', self.sequence)

        # Iterate over all subsequences
        for subsequence in self.sequence[window_indexer]:
            print('\tsubseq =', subsequence)
            name = self._getPattern(subsequence)
            freq[name] += 1 / (self.N - self.w + 1)
        print('')

        return freq

    @staticmethod
    def _getPattern(sequence):
        """
        Convert a list of strings into a string. 
        E.g. ['a', 'b', 'c'] --> 'abc'
        """
        return ''.join(l for l in sequence)
