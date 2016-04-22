class LevenshteinAlgo(object):
    """ Search difference between 2 strings """

    def __init__(self):
        """ Init function for Levenshtein Algorithm """
        print "Levenshtein Algorithm using List"

    def calculateDifference(self,str1,str2):
        """ Calculate Difference of characters in both the string """
        diff = {}
        for i in range(len(str1)):
            diff[i, 0] = i
        for j in range (len(str2)):
            diff[0, j] = j
        for j in range(1,len(str2)):
            for i in range(1,len(str1)):
                if str1[i] == str2[j]:
                    diff[i, j] = d[i-1, j-1]
                else:
                    diff[i, j] = min(diff[i-1, j] + 1, diff[i, j-1] + 1, diff[i-1, j-1] + 1)
        return diff[len(str1)-1, len(str2)-1]

la = LevenshteinAlgo()
print la.calculateDifference(' bombay',' bomb')
