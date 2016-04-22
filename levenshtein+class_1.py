import numpy as np

class LevenshteinAlgo(object):
    """ Search difference between 2 strings """

    def __init__(self):
        """ Init function for Levenshtein Algorithm """
        print "Levenshtein Algorithm using numpy array"


    def calculateDifference(self,str1, str2):
        """ Calculate Difference of characters in both the string """
        if len(str1) < len(str2):
            return levenshtein(str2, str1)

        if len(str2) == 0:
            return len(str1)

        str1 = np.array(tuple(str1))
        str2 = np.array(tuple(str2))

        previous_row = np.arange(str2.size + 1)
        for s in str1:
            current_row = previous_row + 1
            current_row[1:] = np.minimum(
                    current_row[1:],
                    np.add(previous_row[:-1], str2 != s))

            current_row[1:] = np.minimum(
                    current_row[1:],
                    current_row[0:-1] + 1)

            previous_row = current_row

        return previous_row[-1]

la = LevenshteinAlgo()
print la.calculateDifference(' bombay',' bomb')
