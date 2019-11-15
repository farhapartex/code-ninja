class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
    	S, Q = sum([i for i in A if i % 2 == 0]), []
    	for [v,i] in queries:
    		a = A[i]
    		A[i] += v
    		if a % 2 == 0:
    			if v % 2 == 0: S += v
    			else: S -= a
    		elif v % 2 == 1: S += A[i]
    		Q.append(S)
    	return Q