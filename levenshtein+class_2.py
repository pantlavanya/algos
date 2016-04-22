import numpy as np

class LevenshteinAlgo(object):
    """ Search difference between 2 strings """

    def __init__(self):
        """ Init function for Levenshtein Algorithm """
        print "Levenshtein Algorithm using list with shif3"

	def calculateDifference(self,s1,s2, mset=1):
		""" Calculate Difference of characters in both the string s1,s2 """
		if not s1:
			return (not s2 and 0 or len(s2))
		if not s2:
			return len(s1)
		c1 = 0
		c2 = 0
		lcs = 0
		while c1<len(s1) and c2<len(s2):
			if s1[c1] == s2[c2]:
				lcs += 1
			else:
				for i in range(1,mset):
					if c1+i < len(s1) and s1[c1+i] == s2[c2]:
						c1 += i
						break
					if c2+i < len(s2) and s1[c1] == s2[c2+i]:
						c2 += i
						break
			c1 += 1
			c2 += 1
		return ((len(s1)+len(s2))/2-lcs)

la = LevenshteinAlgo()
print la.calculateDifference(' bombay',' bomb')
