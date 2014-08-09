import os, sys


def permutations(l):
	def permut_sub(l1, l2) : 
		if not l2 :
			print(l1)	
		for e in l2 : 
			permut_sub(l1 + [e], [e2 for e2 in l2 if e2 != e ])
	permut_sub([], l)	


def subsets_iteration(l) : 
	n = len(l)
	def bit_rep(m) : 
		while(m):
			remainder= m % 2
			m = m >> 1
			yield remainder
	for i in range(2**n) : 
		print([l[idx] for idx, e in \
			enumerate(reversed(list(bit_rep(i)))) if e])

def subsets_recursion(l):
	def subsets_sub(pre, post):
		if not(post) : 
			print(pre)
			return
		subsets_sub(pre + [post[0]], post[1:])
		subsets_sub(pre, post[1:])
	subsets_sub([], l)

if __name__ == '__main__':
	print("All permutations")
	permutations(range(1,5))
	print("All subsets with iteration")
	subsets_iteration(range(1,5))
	print("All subsets with recursion")
	subsets_recursion(range(1,5))
