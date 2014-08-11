#             1
#      F ---------- E 
#     /\           / \
#  1 /  \10     1 /   \ 10
#   / 10 \   10  /  1  \
#  A ---- G --- H ----- D
#   \    /       \     / 
# 10 \  /10    10 \   / 10
#     \/           \ /
#      B ---------- C
#            10

import sys

def dijkstra(wt, adj, src, target) : 
	processed = set()
	processing = PriorityQueue()
	distance = {}
	parents = {}

	for v in adj.keys():
		distance[v] = sys.maxint

	distance[src] = 0
	processing.push(src, distance[src])
	parents[src] = None

	while(processing) : 
		_, curr = processing.pop()
		processed.add(curr)
	
		for nbr in adj[curr] :
			if nbr in processed : 
				continue
			if distance[nbr] > distance[curr] + wt[curr+nbr] :
				distance[nbr] = distance[curr] + wt[curr+nbr]
				processing.update(nbr, distance[nbr])
				parents[nbr] = curr
	
	def get_path(v) : 
		if v is None : 
			return ""
		return get_path(parents[v]) + v
	
	return get_path(target), distance[target]

class PriorityQueue(object) : 
	""" priority queue implemented as an array """
	def __init__(self) :
		self.q = []
	
	def __len__(self) : 
		return len(self.q) 

	def __nonzero__(self):
		return bool(self.q)

	def __str__(self):
		return self.q.__str__()

	def push(self, key, priority) : 
		if not(self) : 
			insert_idx = 0
		elif self.q[-1][0] <= priority :
			insert_idx = len(self.q)
		else : 
			insert_idx = next(idx for (idx,(p,k)) in enumerate(self.q) if priority < p)
		self.q.insert(insert_idx, (priority,key))

	def update(self, key, priority) : 
		try : 
			update_idx = next(idx for (idx,(p,k)) in enumerate(self.q) if key == priority)	
			self.q.remove(q[update_idx])
		except StopIteration as e : 
			pass
		self.push(key, priority)

	def pop(self):
		if not(self) : 
			raise ValueError("Trying to pop from empty queue")

		return self.q.pop(0)



if __name__ == '__main__' : 
	pq = PriorityQueue()

	#--------------------------------------
	# Testing Priority Queue
	pq.push('A', 3)	
	pq.push('B', 10)	
	pq.push('C', 5)	
	print pq
	pq.update('C',15)
	pq.update('D', 1)
	print pq
	print pq.pop()
	print pq.pop()
	print pq

	#--------------------------------------
	# Create the graph
	adj = {}
	adj["A"] = "FGB"
	adj["B"] = "AGC"
	adj["C"] = "BHD"
	adj["D"] = "CHE"
	adj["E"] = "FHD"
	adj["F"] = "AGE"
	adj["G"] = "AFBH"
	adj["H"] = "GECD"
	
	wt = {}
	wt["AF"] = 1
	wt["AG"] = 10
	wt["AB"] = 10
	wt["BA"] = 10
	wt["BG"] = 10
	wt["BC"] = 10
	wt["CB"] = 10
	wt["CH"] = 10
	wt["DC"] = 10
	wt["DH"] = 1
	wt["DE"] = 10
	wt["ED"] = 10
	wt["EH"] = 1
	wt["EF"] = 1
	wt["FA"] = 1
	wt["FG"] = 10
	wt["FE"] = 1
	wt["GA"] = 10
	wt["GB"] = 10
	wt["GF"] = 10
	wt["GH"] = 10
	wt["HG"] = 10
	wt["HC"] = 10
	wt["HD"] = 1
	wt["HE"] = 1

	print dijkstra(wt, adj, 'A', 'D') 
