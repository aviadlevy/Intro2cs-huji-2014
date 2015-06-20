#!/usr/bin/env python

# Computes the score of the optimal alignment of two DNA strands.
def findOptimalAlignment(strand1,strand2,match,mismatch,gap):
	
	#if we have empty strand then the solution is easy:
	if len(strand1) == 0: return len(strand2) * gap
	if len(strand2) == 0: return len(strand1) * gap

	# There's the scenario where the two leading bases of
	# each strand are forced to align, regardless of whether or not
	# they actually match.
	bestWith = findOptimalAlignment(strand1[1:], strand2[1:],match,mismatch,
                                    gap)
	if strand1[0] == strand2[0]: 
		return bestWith + match # no benefit from making other recursive calls

	best = bestWith + mismatch
	
	# It's possible that the leading base of strand1 best
	# matches not the leading base of strand2, but the one after it.
	bestWithout = findOptimalAlignment(strand1, strand2[1:],match,mismatch,gap)
	bestWithout += gap # penalize for insertion of space
	if bestWithout > best:
		best = bestWithout

	# opposite scenario
	bestWithout = findOptimalAlignment(strand1[1:], strand2,match,mismatch,gap)
	bestWithout += gap # penalize for insertion of space
	if bestWithout > best:
		best = bestWithout

	return best
