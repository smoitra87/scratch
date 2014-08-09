import os, sys
from collections import defaultdict

""" Topsorts
parents is a dict containing nodes as key and list of par as val
childeren is a dict containg nodes as key and list of kids as val
"""
def topsort(parents, children):
	roots = [v for v in parents if not parents[v]]
	topsort_list = []	
	visited = defaultdict(int)

	def dfs(v) : 
		if visited[v] < len(parents[v]) : 
			return

		topsort_list.append(v)
		for child in children[v]:
			visited[child] = visited[child] + 1
			dfs(child)	

	for root in roots : 
		dfs(root)

	for node in topsort_list :  
		print(node)


"""
Create a graph
 1 -> 2 -> 3 -> 7
   \     /
	\   /
 4 -> 5	-> 6

expected order 1 4 2 3 7 5 6
"""
if __name__ == '__main__'  :
	parents = {
	 	1 : [],
		2 : [1],
		3 : [2],
		4 : [],
		5 : [4, 3], 
		6 : [5],
		7 : [6]
	}

	children = {
		1 : [2],
		2 : [3],
		3 : [5, 7],
		4 : [5],
		5 : [6],
		6 : [],
		7 : []
	}


	topsort(parents, children)

