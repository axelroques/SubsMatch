
from .histogram import Histogram
from .sax import SAX


class SubsMatch:

    def __init__(self, sequences, a, w) -> None:
        """
        Inputs:
            - sequences = tuple of sequences to compare
            - a = size of the discrete alphabet
            - w = size of the window / size of the 
            subsequences to find.
        """

        self.sequences = sequences
        self.a = a
        self.w = w

    def process(self):
        """
        Processing pipeline for the SubsMatch algorithm.
        """

        # SAX representation of the input sequences
        self.sequences_SAX = SAX(self.sequences)
        print('Input sequences =', self.sequences)
        print('SAX sequences =', self.sequences_SAX, '\n')

        # Compute histograms
        H_1 = Histogram(self.sequences_SAX[0], self.w)
        H_2 = Histogram(self.sequences_SAX[1], self.w)
        self.histograms = (H_1, H_2)
        print('Histogram 1 =', H_1.table)
        print('\tTotal =', sum(H_1.table.values()))
        print('Histogram 2 =', H_2.table)
        print('\tTotal =', sum(H_2.table.values()), '\n')

        # Compute distance between histograms
        self.d = H_1.distance(H_2)
        print('Distance =', self.d, '\n')

        # Compute similarity
        self.similarity = 1 - self.d
        print('--> Similarity =', self.similarity, '\n')

        return
